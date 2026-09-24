# make_redirects.py  (run in the root of the intsav clone)
from pathlib import Path
import shutil

BASE = "https://www.thrive-centre.com"
PROJ = "/projects"      # adjust if thrive uses a different prefix

REDIRECTS = {
    "biobank.html":                    "/datasets/",

    # standalone projects
    "electroglottography.html":        f"{PROJ}/electroglottography/",
    "PulseNote.html":                  f"{PROJ}/pulsenote/",
    "Risk_Assessment_ED.html":         f"{PROJ}/Risk_Assessment_ED/",
    "sclerosis.html":                  f"{PROJ}/sclerosis/",
    "seizure_detection.html":          f"{PROJ}/seizure_detection/",
    "seizure_detection2.html":         f"{PROJ}/seizure_detection/",
    "spinal.html":                     f"{PROJ}/spinal/",
    "tbi.html":                        f"{PROJ}/tbi/",

    # unity
    "unitylv-multix.html":             f"{PROJ}/unity/",
    "efficient_annotations.html":      f"{PROJ}/unity/Efficient_Annotations/",
    "loss.html":                       f"{PROJ}/unity/Loss_Functions/",
    "Influence of Loss Functions.html":f"{PROJ}/unity/Loss_Functions/",
    "lv_segmentation.html":            f"{PROJ}/unity/LV_Segmentation/",
    "phase_detection.html":            f"{PROJ}/unity/phase_detection/",
    "speckle_tracking.html":           f"{PROJ}/unity/speckle_tracking/",
    "tdi.html":                        f"{PROJ}/unity/TDI/",
    "view_classification.html":        f"{PROJ}/unity/View_Classification/",
    "view-detection.html":             f"{PROJ}/unity/View_Classification/",
}

STUB = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Redirecting…</title>
  <link rel="canonical" href="{url}">
  <meta http-equiv="refresh" content="0; url={url}">
  <script>location.replace("{url}");</script>
</head>
<body>
  <p>Moved to <a href="{url}">{url}</a>.</p>
</body>
</html>
"""

for old, new in REDIRECTS.items():
    p = Path(old)
    if not p.exists():
        print(f"skip (not found): {old}")
        continue
    archive = Path(f"archive-{old}")
    if not archive.exists():
        shutil.copy(p, archive)
        html = archive.read_text(encoding="utf-8", errors="ignore")
        if "noindex" not in html:
            html = html.replace("<head>", '<head>\n<meta name="robots" content="noindex">', 1)
            archive.write_text(html, encoding="utf-8")
    p.write_text(STUB.format(url=BASE + new), encoding="utf-8")
    print(f"{old} -> {BASE + new}")