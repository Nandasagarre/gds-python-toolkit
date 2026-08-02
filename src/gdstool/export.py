from pathlib import Path
import csv
from src.gdstool.models import ShapeInfo

def export_shapes_csv(shapes: list[ShapeInfo], output_file: Path):
    """Export extracted shapes to CSV."""

    with open(output_file, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(
            [
                "Cell",
                "Layer",
                "Datatype",
                "ShapeType",
                "Width",
                "Height",
                "Area",
                "Left",
                "Bottom",
                "Right",
                "Top",
            ]
        )

        for shape in shapes:

            box = shape.bbox

            writer.writerow([
                shape.cell,
                shape.layer,
                shape.datatype,
                shape.shape_type,
                shape.width,
                shape.height,
                shape.area,
                shape.bbox.left,
                shape.bbox.bottom,
                shape.bbox.right,
                shape.bbox.top,
            ])