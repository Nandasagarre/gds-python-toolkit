import pya


def get_polygon_points(shape: pya.Shape) -> list[tuple[int, int]]:
    """Return vertices of a box or polygon."""

    if shape.is_box():

        box = shape.box

        return [
            (box.left, box.bottom),
            (box.left, box.top),
            (box.right, box.top),
            (box.right, box.bottom),
        ]

    elif shape.is_polygon():

        polygon = shape.polygon

        return [(pt.x, pt.y) for pt in polygon.each_point_hull()]

    return []