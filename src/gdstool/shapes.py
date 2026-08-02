import pya

from src.gdstool.geometry import get_bbox
from src.gdstool.polygons import get_polygon_points

def list_shapes(layout: pya.Layout):
    """List all shapes in the top cell."""

    top = layout.top_cell()
    for layer_index in layout.layer_indexes():

        layer_info = layout.get_info(layer_index)

        print(f"\nLayer {layer_info.layer}/{layer_info.datatype}")

        for shape in top.shapes(layer_index):

            bbox = get_bbox(shape, layout.dbu)

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

        print(
            f"{shape_type:8}"
            f" DBU: ({bbox['left']}, {bbox['bottom']}) -> ({bbox['right']}, {bbox['top']})"
            f" | µm: ({bbox['left_um']:.3f}, {bbox['bottom_um']:.3f})"
            f" -> ({bbox['right_um']:.3f}, {bbox['top_um']:.3f})"
        )

        if shape.is_box() or shape.is_polygon():
            points = get_polygon_points(shape)
            print("         Vertices:", points)