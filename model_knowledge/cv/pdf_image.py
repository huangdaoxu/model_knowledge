import fitz
import logging

from model_knowledge.cv.ocr import ocr


logger = logging.getLogger("default")


def extract_images(file):
    """
    extract images from pdf
    :param file: file absolute path
    :return: image binary io iterator
    """
    with fitz.open(file) as pdf:
        for page in pdf:
            try:
                # 扩大像素2倍
                mat = fitz.Matrix(2.0, 2.0)
                yield page.get_pixmap(matrix=mat).tobytes()
            except Exception as e:
                logger.exception(e)


def image2txt(file):
    text = ''
    images = extract_images(file=file)
    for image in images:
        text += ocr(image)
    return text