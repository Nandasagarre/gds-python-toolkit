import pya


def bbox_width(box: pya.Box) -> int:
    return box.width()


def bbox_height(box: pya.Box) -> int:
    return box.height()


def bbox_area(box: pya.Box) -> int:
    return box.width() * box.height()


def bbox_perimeter(box: pya.Box) -> int:
    return 2 * (box.width() + box.height())