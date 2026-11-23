import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
import json, sys, asyncio, re, os
from playwright.async_api import async_playwright
F = GCW + "ds/project/fonts/"
CSS = f"""@font-face{{font-family:Engram;src:url(file://{F}engram-regular.woff2)}}
@font-face{{font-family:'Engram ExtraBold';src:url(file://{F}engram-extrabold.woff2)}}
@font-face{{font-family:'Engram Bold';src:url(file://{F}engram-bold.woff2)}}
@font-face{{font-family:'Engram Medium';src:url(file://{F}engram-medium.woff2)}}
body{{margin:0}} section{{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box}}
section *{{margin:0;box-sizing:content-box}} aside{{display:none}}
x-icon{{display:inline-block;background:currentColor;border-radius:4px}}"""
async def main(d):
    b = json.load(open(f"{d}/build.json"))
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg = await br.new_page(viewport={"width": 1920, "height": 1080})
        os.makedirs(f"{d}/prev", exist_ok=True)
        for i, sid in enumerate(b["order"], 1):
            h = open(f"{d}/project/slides/{sid}.html").read()
            for k, v in b["assets"].items(): h = h.replace("{{" + k + "}}", "file://" + v)
            open("/tmp/_prev.html","w").write(f"<html><head><style>{CSS}</style></head><body>{h}</body></html>")
            await pg.goto("file:///tmp/_prev.html"); await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"{d}/prev/{i:02d}-{sid}.png")
        await br.close()
asyncio.run(main(sys.argv[1]))
