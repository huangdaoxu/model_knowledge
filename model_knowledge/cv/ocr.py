import io
import os
import torch
import numpy as np

from cnocr import CnOcr
from pathlib import Path
from PIL import Image
from typing import Union

from model_knowledge.utils.tools import timeit

_rec_model_path = Path(os.path.dirname(__file__)).parent / 'data' / 'ocr' / 'densenet_lite_136-fc' / \
                  'cnocr-v2.2-densenet_lite_136-fc-epoch=039-complete_match_epoch=0.8597-model.onnx'
_det_model_path = Path(os.path.dirname(__file__)).parent / 'data' / 'ocr' / 'ppocr' / \
                  'ch_PP-OCRv3_det_infer.onnx'
_ocr = CnOcr(rec_model_fp=str(_rec_model_path), det_model_fp=str(_det_model_path))  # 所有参数都使用默认值


# @timeit
def ocr(img_fp: Union[str, bytes, Image.Image, torch.Tensor, np.ndarray], aligning=True,
        aligning_threshold=5):
    """
    Optical Character Recognition
    :param img_fp: image file path;
                or image file bytes;
                or loaded image by `Image.open()`;
                or color image torch.Tensor or np.ndarray,
                    with shape [height, width] or [height, width, channel].
                    channel should be 1 (gray image) or 3 (RGB formatted color image). scaled in [0, 255];
    :param aligning: Whether to enable automatic alignment;
    :param aligning_threshold: Residual threshold for aligning;
    :return: list of detected texts, which element is a dict, with keys:
                - 'text' (str)
                - 'score' (float)
                - 'position'
                - 'cropped_img'
    """
    if isinstance(img_fp, bytes):
        img_fp = Image.open(io.BytesIO(img_fp))
        img_fp.show()
    res = _ocr.ocr(img_fp)
    if aligning:
        text = res[0].get('text', '') if res else ''
        for ind in range(0, len(res) - 1, 1):
            line_pos = res[ind].get('position', [])
            next_line_pos = res[ind + 1].get('position', [])
            if next_line_pos[0][1] - line_pos[0][1] <= aligning_threshold and \
                    next_line_pos[3][1] - line_pos[3][1] <= aligning_threshold:
                text += ' ' + res[ind + 1].get('text', '')
            else:
                text += '\n' + res[ind + 1].get('text', '')
    else:
        text = '\n'.join([i.get('text', '') for i in res])
    return text
