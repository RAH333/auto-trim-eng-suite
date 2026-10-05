# auto-trim-eng-suite
Parametric Automotive Plastic Trim Design Engine & Optimization Suite. 

This shows more than standard 3D CAD modeling. Since automotive plastic trims require complex engineering documentation, creating a structured, automated tool to handle engineering calculations, quality checkpoints, and cross-functional reviews is an exceptional way to showcase depth.


It automates standard plastic design rules (draft angles, rib thicknesses, and doghouse dimensions), maps engineering data, and calculates assembly specifications directly linked to a Bill of Materials (BOM).

# Automated Automotive Plastic Trim Parametric Validator Engine
> **Target Role Application:** Lead Engineer - Trims Engineering CoE (Mahindra & Mahindra Ltd.)

This repository hosts an engineering utility engine configured to parse, evaluate, and structure design parameter data profiles against strict injection-molding plastics design standards.

## Features & Engineering Implementation
1. **Automated Design Verification Rules (`src/core_rules.py`):** Codifies critical mechanical criteria including nominal wall relationships, draft angles, and clip placement spacing.
2. **Manufacturing BOM Structure Engine (`src/bom_generator.py`):** Organizes interior components into structured BOM sheets specifying tracking IDs, material types (PP-TD20, ABS, PC+ABS), and mass properties.
3. **Automated Gateway Quality Controls:** Integrated with GitHub Actions CI workflows (`.github/workflows/validation.yml`) acting as virtual program milestone gateways.

## Getting Started & Execution
Execute validation evaluations inside terminal environments via:
```bash
pip install -r requirements.txt
python src/main.py
```

To initiate automated verification test sequences:
```bash
pytest tests/
```


```
auto-trim-eng-suite/
│
├── .github/
│   └── workflows/
│       └── validation.yml
│
├── docs/
│   ├── DFMEA_Template.md
│   ├── DVP_Template.md
│   └── Master_Sections.pdf
│
├── src/
│   ├── __init__.py
│   ├── core_rules.py
│   ├── bom_generator.py
│   └── main.py
│
├── tests/
│   └── test_rules.py
│
├── requirements.txt
└── README.md
```
