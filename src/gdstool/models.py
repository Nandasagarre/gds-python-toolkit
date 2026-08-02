from dataclasses import dataclass
import pya


@dataclass
class LayoutInfo:
    dbu: float
    top_cell: str
    num_cells: int
    num_layers: int


@dataclass
class LayerInfo:
    layer: int
    datatype: int
    name: str


@dataclass
class LayerCount:
    layer: int
    datatype: int
    count: int


@dataclass
class ShapeInfo:
    cell: str
    layer: int
    datatype: int
    shape_type: str
    bbox: pya.Box
    width: int
    height: int
    area: int