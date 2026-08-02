from pathlib import Path
import pya
from src.gdstool.models import LayoutInfo

def get_layout_info(layout: pya.Layout) -> dict:
    """Return basic layout information."""

    return LayoutInfo(
        dbu=layout.dbu,
        top_cell=layout.top_cell().name,
        num_cells=layout.cells(),
        num_layers=layout.layers(),
    )