import cv2
import numpy as np
import os

from pathlib import Path
from typing import Tuple, AnyStr


_model_path = Path(os.path.dirname(__file__)).parent / 'data' / 'qrcode'
_qr_decoder = cv2.wechat_qrcode_WeChatQRCode(
    str(_model_path / "detect.prototxt"), str(_model_path / "detect.caffemodel"),
    str(_model_path / "sr.prototxt"), str(_model_path / "sr.caffemodel"))


def get_qrcode_content(pic: AnyStr) -> Tuple[str]:
    """
    get qrcode content from picture
    :param pic: picture path or binary bytes
    :return: tuple(content1, content2, ...)
    """
    if isinstance(pic, str):
        image = cv2.imread(pic)
    elif isinstance(pic, bytes):
        # 二进制数据流转cv2
        image = cv2.imdecode(np.frombuffer(pic, np.uint8), cv2.IMREAD_COLOR)
    else:
        raise ValueError('pic is not anystr')
    res, _ = _qr_decoder.detectAndDecode(image)
    return res
