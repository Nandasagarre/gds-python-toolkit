from pathlib import Path

from src.gdstool.io import load_layout
from src.gdstool.layout import get_layout_info


def main():

    gds_path = Path("data/input/inv.gds")

    layout = load_layout(gds_path)

    info = get_layout_info(layout)

    print("\nLayout Information")
    print("------------------")

    for key, value in info.items():
        print(f"{key:12}: {value}")


if __name__ == "__main__":
    main()