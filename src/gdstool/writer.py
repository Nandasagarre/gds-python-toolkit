from pathlib import Path
import pya


def write_layout(layout: pya.Layout, output_path: Path):
    """Write the layout to a GDSII file."""

    layout.write(str(output_path))