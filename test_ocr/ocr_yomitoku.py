# -*- coding: utf-8 -*-
import cv2
import os
from pathlib import Path
from yomitoku import DocumentAnalyzer, OCR
from yomitoku.data.functions import load_pdf

BASE_DIR = Path(__file__).parent
OUT_DIR = BASE_DIR / "results" / "yomitoku"

PATH_IMG = "images/demo.jpg"
ext = os.path.splitext(PATH_IMG)[1].lower()
# .splitext で拡張子を所得（.付き）、lower で小文字化

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
        print(results.words[0].points)
        results.to_json(f"{OUT_DIR}/output_{i}.json")
