# GDS Python Toolkit

A Python toolkit for exploring, analyzing, and manipulating GDSII layouts using the KLayout Python API. The project is structured as a modular, reusable library rather than a collection of standalone scripts.

## Scope

- Read and validate GDSII files
- Explore layout hierarchy
- Inspect cells, layers, and shapes
- Extract geometry and statistics
- Perform basic geometry operations
- Build utilities useful for mask data preparation (MDP) workflows

## Current Features

- ✔ Load GDSII layouts
- ✔ Layout information (DBU, top cell, cell/layer count)
- ✔ Enumerate layers
- ✔ Enumerate cells and hierarchy
- ✔ Count shapes by layer
- ✔ Modular project structure

## Planned Features

- Shape extraction (Box, Polygon, Path, Text)
- Hierarchy traversal utilities
- Bounding box extraction
- Area and density calculation
- Layer filtering
- Boolean geometry operations
- Layout flattening
- CSV/JSON reporting
- GDS writer
- Ring Oscillator layout case study
- Mask Job Deck generation
- Basic Mask Data Preparation utilities

## Project Structure

```text
gds-python-toolkit/
├── data/
├── docs/
├── scripts/
├── src/
│   └── gdstool/
├── tests/
└── main.py
```

## Tech Stack

- Python 3
- KLayout Python API (`pya`)
- Git
- VS Code

## Status

🚧 Active development

Current focus:
- Build reusable GDS analysis APIs
- Understand the KLayout database model
- Progress toward an end-to-end mask preparation workflow

## Long-Term Goal

Develop a professional-quality open-source toolkit for:
- Layout Engineering
- Photomask Engineering
- Mask Data Preparation (MDP)
- Semiconductor CAD Automation
