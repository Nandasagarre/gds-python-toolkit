from src.gdstool.models import ShapeInfo


def filter_by_layer(
    shapes: list[ShapeInfo],
    layer: int,
    datatype: int = 0,
) -> list[ShapeInfo]:
    """Return shapes on the specified layer/datatype."""

    return [
        shape
        for shape in shapes
        if shape.layer == layer and shape.datatype == datatype
    ]