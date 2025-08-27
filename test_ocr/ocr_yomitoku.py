# -*- coding: utf-8 -*-
import cv2
import os
from pathlib import Path
from yomitoku import DocumentAnalyzer, OCR
from yomitoku.data.functions import load_pdf
from huggingface_hub import snapshot_download

BASE_DIR = Path(__file__).parent
OUT_DIR = BASE_DIR / "results" / "yomitoku"
PATH_IMG = BASE_DIR /"images/demo.jpg"
ext = os.path.splitext(PATH_IMG)[1].lower()
# .splitext で拡張子を所得（.付き）、lower で小文字化

os.environ.setdefault("HUGGINGFACE_HUB_CACHE", str(BASE_DIR / "models")) 
for repo in [
    "KotaroKinoshita/yomitoku-text-detector-dbnet-open-beta",
    "KotaroKinoshita/yomitoku-text-recognizer-parseq-open-beta",
]:
    snapshot_download(repo_id=repo)


def load_image(path):
    if ext == ".pdf":
        imgs = load_pdf(path)
    else:
        img = cv2.imread(path)
        imgs = [img]
    return imgs


if __name__ == "__main__":
    configs = {
        "text_detector":   {"path_cfg": str(BASE_DIR/"models"/"yomitoku"/"text_detector.yaml")},
        "text_recognizer": {"path_cfg": str(BASE_DIR/"models"/"yomitoku"/"text_recognizer.yaml")},
    }

    analyzer = DocumentAnalyzer(configs=configs, visualize=False, device="auto")
    
    imgs = load_image(PATH_IMG)
    
    for i, img in enumerate(imgs):
        results, _,_  = analyzer(img)
        for w in results.words:
            points = w.points 
            #[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
            content = w.content
            direction = w.direction
            rec_score = w.rec_score
            det_score = w.det_score
        results.to_json(f"{OUT_DIR}/output_{i}.json")
