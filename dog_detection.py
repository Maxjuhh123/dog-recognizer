from typing import List

import numpy as np

from common.BoundingBox import BoundingBox


def detect_dogs(img: np.ndarray) -> List[(BoundingBox, str)]:
    """
    Detect and recognize dogs and their breeds in an image.

    :param img: The image
    :return: A list of pairs of detected bounding boxes around the dogs and their labels (breeds)
    """
    print(img)

    return None
