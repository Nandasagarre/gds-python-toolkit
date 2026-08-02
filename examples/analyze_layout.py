from src.gdstool.io import load_layout
from src.gdstool.layout import get_layout_info
from src.gdstool.layers import get_layers, count_shapes
from src.gdstool.cells import list_cells
from src.gdstool.shapes import list_shapes
from src.gdstool.extractor import extract_shapes
from src.gdstool.statistics import layer_statistics
from src.gdstool.filter import filter_by_layer


def print_header(title):
    print(f"\n=== {title} ===")


layout = load_layout("data/input/inv.gds")

print_header("Layout Information")
for k, v in vars(get_layout_info(layout)).items():
    print(f"{k:12}: {v}")

print_header("Layers")
for layer in get_layers(layout):
    print(f"{layer.layer}/{layer.datatype}")

print_header("Shape Count")
for shape in count_shapes(layout):
    print(f"{shape.layer}/{shape.datatype}: {shape.count}")

print_header("Cell Hierarchy")
list_cells(layout)

print_header("Shapes")
list_shapes(layout)

shapes = extract_shapes(layout.top_cell(), layout)

print_header("Layer Statistics")
for (layer, datatype), count in sorted(layer_statistics(shapes).items()):
    print(f"{layer}/{datatype}: {count}")

print_header("Filter Layer 34/0")
for shape in filter_by_layer(shapes, 34)[:5]:
    print(shape)