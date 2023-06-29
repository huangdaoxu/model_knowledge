import os

from pathlib import Path

from model_knowledge.cv.ocr import ocr
from model_knowledge.cv.qrcode import get_qrcode_content


def qrcode_example():
    img_fp = Path(os.path.dirname(__file__)).parent / 'data' / 'static' / 'qrcode_test.png'
    res = get_qrcode_content(str(img_fp))
    print(res)


def ocr_example():
    img_fp = Path(os.path.dirname(__file__)).parent / 'data' / 'static' / 'ocr_test.jpeg'
    res = ocr(str(img_fp), aligning=True)
    print(res)


if __name__ == "__main__":
    qrcode_example()
    ocr_example()
