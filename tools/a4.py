"""Rebuild A4 pages from the Carlsberg/Tesco deck as 16:9 plates.
render(page_no, keep) renders the page's colour area at 969px tall, with every text block removed except those
where keep(text, bbox) is true. widen(img, x, width) inserts a flat strip copied from column x."""
import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
import fitz, numpy as np
from PIL import Image
PDF = "/mnt/user-data/uploads/Downloads/PDFs/GC_Tesco_Deck.pdf"
BOTTOM = None


def colour_bottom(doc):
    p = doc[6]; pix = p.get_pixmap(dpi=72)
    a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3)
    for y in range(300, pix.height):
        if a[y, 5].min() > 245: return y
    return 533


def render(n, keep=lambda t, b: False, drop_images=(), supersample=2, paint=(), bg_at=(20, 20), pad=4, cover=True, fill=(), keep_yellow=False):
    """paint: extra rects (pt) to fill with the background colour; removed text blocks are filled too when cover."""
    doc = fitz.open(PDF); p = doc[n - 1]
    bottom = colour_bottom(doc) - 1
    rects = list(paint)
    for b in p.get_text("dict")["blocks"]:
        if b["type"] != 0: continue
        txt = " ".join(s["text"] for l in b["lines"] for s in l["spans"])
        if not keep(txt, b["bbox"]):
            p.add_redact_annot(fitz.Rect(b["bbox"]))
            if cover and b["bbox"][1] < bottom: rects.append(b["bbox"])
    p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE, text=fitz.PDF_REDACT_TEXT_REMOVE)
    for x in drop_images:
        try: p.delete_image(x)
        except Exception as e: print("drop failed", x, e)
    s = 969 / bottom * supersample
    pix = p.get_pixmap(matrix=fitz.Matrix(s, s), clip=fitz.Rect(0, 0, p.rect.width, bottom))
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    im = im.resize((round(pix.width / supersample), 969), Image.LANCZOS)
    k = 969 / bottom; a = np.array(im); orig = a.copy()
    col = a[round(bg_at[1] * k), round(bg_at[0] * k)].copy()
    for (x0, y0, x1, y1) in rects:
        a[max(0, round((y0 - pad) * k)):round((y1 + pad) * k), max(0, round((x0 - pad) * k)):round((x1 + pad) * k)] = col
    if keep_yellow:   # rings the text cover clipped come back from the uncovered render
        o = orig.astype(int); yel = (o[..., 0] > 200) & (o[..., 1] > 180) & (o[..., 2] < 110)
        from scipy import ndimage
        yel = ndimage.binary_dilation(yel, iterations=2) & (np.abs(o - o[5, 5]).sum(2) > 30)
        a[yel] = orig[yel]
    for (x0, y0, x1, y1), (sx, sy) in fill:
        c2 = a[round(sy * k), round(sx * k)].copy()
        a[round(y0 * k):round(y1 * k), round(x0 * k):round(x1 * k)] = c2
    return Image.fromarray(a), k


def widen(im, x, width):
    a = np.array(im); col = a[:, x:x + 1]
    strip = np.repeat(col, width, axis=1)
    return Image.fromarray(np.concatenate([a[:, :x], strip, a[:, x:]], axis=1))


def flat_columns(im, lo, hi, tol=6):
    a = np.array(im).astype(int)
    out = []
    for x in range(lo, hi):
        c = a[:, x]; 
        if (np.abs(c - c[0]).sum(1).max()) <= tol: out.append(x)
    return out


def homog_columns(im, lo, hi, w=3, tol=8, rows=None):
    """Columns where every row is the same colour for w px either side, so repeating the column leaves no seam."""
    a = np.array(im).astype(int)
    if rows is not None: a = a[rows[0]:rows[1]]
    out = []
    for x in range(max(lo, w), min(hi, a.shape[1] - w)):
        blk = a[:, x - w:x + w + 1]
        if np.abs(blk - a[:, x:x + 1]).sum(2).max() <= tol: out.append(x)
    return out


def widen_many(im, cuts):
    """cuts: [(x, width)], x in the original image."""
    a = np.array(im); parts = []; last = 0
    for x, wd in sorted(cuts):
        parts.append(a[:, last:x]); parts.append(np.repeat(a[:, x:x + 1], wd, axis=1)); last = x
    parts.append(a[:, last:])
    return Image.fromarray(np.concatenate(parts, axis=1))
