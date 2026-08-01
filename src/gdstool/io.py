from pathlib import Path
import pya


def load_layout(file_path: Path) -> pya.Layout:
    """Load a GDSII file."""

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    layout = pya.Layout()
    layout.read(str(file_path))

    return layout