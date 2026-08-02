import pya

from src.gdstool.models import ShapeInfo
from src.gdstool.metrics import (
    bbox_width,
    bbox_height,
    bbox_area,
)


def extract_shapes(
    cell: pya.Cell,
    layout: pya.Layout,
    results: list[ShapeInfo] | None = None,
) -> list[ShapeInfo]:
    """Extract all shapes from a cell hierarchy."""

    if results is None:
        results = []

    for layer_index in layout.layer_indexes():

        layer_info = layout.get_info(layer_index)

        for shape in cell.shapes(layer_index):

            if shape.is_box():
                shape_type = "Box"
            elif shape.is_polygon():
                shape_type = "Polygon"
            elif shape.is_path():
                shape_type = "Path"
            elif shape.is_text():
                shape_type = "Text"
            else:
                shape_type = "Other"

            box = shape.bbox()

            results.append(
                ShapeInfo(
                    cell=cell.name,
                    layer=layer_info.layer,
                    datatype=layer_info.datatype,
                    shape_type=shape_type,
                    bbox=box,
                    width=bbox_width(box),
                    height=bbox_height(box),
                    area=bbox_area(box),
                )
            )

    for inst in cell.each_inst():
        extract_shapes(inst.cell, layout, results)

    return results