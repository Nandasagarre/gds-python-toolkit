import pya


def get_bbox(shape: pya.Shape):

    box = shape.bbox()

import pya


def get_bbox(shape: pya.Shape, dbu: float) -> dict:
    """Return the bounding box in DBU and microns."""

    box = shape.bbox()

    return {
        "left": box.left,
        "bottom": box.bottom,
        "right": box.right,
        "top": box.top,
        "left_um": box.left * dbu,
        "bottom_um": box.bottom * dbu,
        "right_um": box.right * dbu,
        "top_um": box.top * dbu,
    }