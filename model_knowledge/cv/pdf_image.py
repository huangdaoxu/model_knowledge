import fitz
import io
import logging

from PIL import Image

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


def image2txt(file, bbox=None):
    text = ''
    images = extract_images(file=file)
    for image in images:
        image = Image.open(io.BytesIO(image))
        if bbox:
            box = (bbox[0] * image.width, bbox[1] * image.height,
                   (1 - bbox[2]) * image.width, (1 - bbox[3]) * image.height)
            image = image.crop(box)
        text += ocr(image)
    return text
