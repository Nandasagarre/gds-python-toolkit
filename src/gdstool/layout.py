from pathlib import Path
import pya


def get_layout_info(layout: pya.Layout) -> dict:
    """Return basic layout information."""

    return {
        "dbu": layout.dbu,
        "top_cell": layout.top_cell().name,
        "num_cells": layout.cells(),
        "num_layers": layout.layers(),
    }