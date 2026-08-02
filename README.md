# GDS Python Toolkit

A lightweight Python toolkit for reading, analyzing, editing, and writing GDSII layouts using the KLayout Python API.

The project is designed as a reusable Python library for GDSII manipulation and serves as a foundation for future Mask Data Preparation (MDP) and semiconductor CAD automation projects.

---

## Features

### Layout Analysis

- Read GDSII layouts
- Inspect layout information
- Enumerate layers
- Enumerate cells and hierarchy
- Count shapes by layer
- Extract layout geometry
- Compute basic geometry metrics
- Generate layer statistics
- Filter shapes by layer

### Layout Editing

- Create new layers
- Insert rectangular geometry
- Move geometry
- Delete layer geometry
- Duplicate cells
- Write modified GDSII layouts

### Export

- Export extracted geometry to CSV

---

## Examples

```bash
# Analyze a layout
python -m examples.analyze_layout

# Export geometry to CSV
python -m examples.export_csv

# Edit a layout and write a new GDS
python -m examples.edit_layout
```

---

## Project Structure

```text
gds-python-toolkit/
├── data/
│   ├── input/
│   └── output/
├── docs/
├── examples/
├── src/
│   └── gdstool/
├── tests/
├── main.py
└── README.md
```

---

## Technology

- Python 3
- KLayout Python API
- Git
- VS Code

---

## Repository Scope

This repository focuses on generic GDSII operations:

- Reading and writing layouts
- Geometry extraction
- Layout inspection
- Basic editing
- Data export

Advanced Mask Data Preparation algorithms (biasing, density analysis, fracture, OPC, etc.) are intentionally kept outside the scope of this repository and will be implemented in dedicated projects.

---

## Future Work

- Additional geometry editing operations
- Improved CLI
- Unit tests
- API documentation
- Package distribution (`pip`)

---

## License

MIT License
