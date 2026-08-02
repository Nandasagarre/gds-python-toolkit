from src.gdstool.cli import parse_args
from src.gdstool.io import load_layout


def main():
    args = parse_args()
    layout = load_layout(args.input)
    print(f"Loaded '{args.input}' successfully.")
    print(f"Top Cell : {layout.top_cell().name}")
    print(f"Layers   : {layout.layers()}")
    print(f"Cells    : {layout.cells()}")


if __name__ == "__main__":
    main()