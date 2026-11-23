import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
import sys; sys.path.insert(0, GCW + 'tools'); import a4
OUT = GCW + "plates/a4"
BASE = lambda t, b: False   # the sensory box is cropped out whole and placed as its own picture
BOX = (272, 258, 460, 380)
CFG = {
    6: (dict(), [(900, 392)]),
    7: (dict(paint=[(40, 280, 64, 412)]), [(400, 392)]),
    9: (dict(paint=[(40, 300, 64, 455), (236, 306, 249, 320), (236, 381, 249, 395)], keep_yellow=True), [(400, 392)]),
    11: (dict(keep=lambda t, b: b[0] > 380 and b[1] < 450), [(300, 392)]),
    14: (dict(keep=BASE, paint=[(40, 255, 62, 385), BOX], fill=[((0, 112.0, 455.6, 146.0), (400, 128))]), [(600, 300), (1510, 92)]),
    15: (dict(keep=BASE, paint=[(40, 255, 62, 385), BOX], fill=[((0, 112.0, 455.6, 146.0), (400, 128))]), [(600, 300), (1510, 92)]),
    16: (dict(keep=BASE, paint=[(40, 255, 62, 385), (40, 470, 200, 490), BOX], fill=[((0, 112.0, 455.6, 146.0), (400, 128))]), [(600, 300), (1510, 92)]),
    17: (dict(keep=BASE, paint=[(40, 255, 62, 385), BOX], fill=[((0, 112.0, 455.6, 146.0), (400, 128))]), [(600, 300), (1510, 92)]),
    13: (dict(keep=lambda t, b: b[1] > 200), [(40, 196), (1490, 196)]),
}
CUTS = {n: c for n, (_, c) in CFG.items()}
CUTS[12] = [(190, 98), (575, 98), (956, 98), (1512, 98)]
K = 969 / 533


def X(n, pt):
    """Slide x for a point x on the A4 page."""
    px = pt * K
    return round(px + sum(w for x, w in CUTS[n] if x <= px))


def Y(pt): return round(pt * K)


if __name__ == "__main__":
    for n, (kw, cuts) in CFG.items():
        if n == 12: continue
        im, k = a4.render(n, **kw)
        im = a4.widen_many(im.crop((0, 0, 1528, 969)), cuts)
        assert im.size == (1920, 969), (n, im.size)
        im.save(f"{OUT}/w{n}.jpg", quality=88); print(n, "ok")
        if n in (14, 15, 16, 17):
            full, k = a4.render(n, keep=lambda t, b: True, cover=False)
            x0, y0, x1, y1 = [round(v * K) for v in BOX]
            a = __import__("numpy").array(full)
            # tight crop to the yellow box
            import numpy as np
            sub = a[y0:y1, x0:x1].astype(int); yel = (sub[..., 0] > 220) & (sub[..., 2] < 90)
            ys, xs = np.nonzero(yel)
            full.crop((x0 + xs.min(), y0 + ys.min(), x0 + xs.max() + 1, y0 + ys.max() + 1)).save(f"{OUT}/box{n}.png")
