from pathlib import Path

from src.gdstool.io import load_layout
from src.gdstool.extractor import extract_shapes
from src.gdstool.export import export_shapes_csv


layout = load_layout("data/input/inv.gds")

shapes = extract_shapes(
    layout.top_cell(),
    layout,
)

output = Path("data/output/shapes.csv")

export_shapes_csv(shapes, output)

print(f"CSV written to {output}")