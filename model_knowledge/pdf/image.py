import fitz
import logging


logger = logging.getLogger("default")


def extract_images(file):
    """
    extract images from pdf
    :param file: file absolute path
    :return: image binary io iterator
    """
    img_count = 0
    with fitz.open(file) as pdf:
        len_xref = pdf.xref_length()
        logger.debug("文件名:{}, 页数: {}, 对象: {}".format(file, len(pdf), len_xref - 1))

        for page in pdf:
            try:
                img_count += 1
                images = page.get_images()
                for xref in images:
                    xref = xref[0]
                    img = pdf.extract_image(xref)
                    yield img["image"]
            except Exception as e:
                logger.exception(e)

