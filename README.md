# Petaluma Residence — Main House CAD Plans

## Current drawing set

**Revision 60 (v60)** is the current baseline. The editable DXF is the source of record; the accompanying seven-page A3 PDF is a review/print copy. Do not modify PDF linework and treat it as an updated CAD source.

The drawing covers the existing main-house floor plan, room labels, windows, doors, master bathroom/walk-in closet inset, and internal/external dimensions. The design has been developed iteratively; review against actual site conditions before relying on individual measurements.

## Drawing sheets

| Sheet | Content | Scale |
| --- | --- | --- |
| A-001 | Overall plan, exterior wall-centerline dimensions | 1:100 @ A3 landscape |
| A-002 | Internal clear widths — west/central spaces | 1:75 @ A3 landscape |
| A-003 | Internal clear widths — bedroom wing | 1:75 @ A3 landscape |
| A-004 | Internal clear depths — west/central spaces | 1:75 @ A3 landscape |
| A-005 | Internal clear depths — bedroom wing | 1:75 @ A3 landscape |
| A-006 | Room dimension schedule | Tabular |
| A-007 | Combined exterior and internal dimensions | 1:100 @ A3 landscape |

Print at **100% on A3 landscape (420 × 297 mm)**; scaling to fit other paper sizes changes the printed scale.

## CAD structure

The DXF includes `Model` (editable source geometry) and seven `A-00x A3` paper-space layouts. In v60 the sheets contain paper-space copies of drawing geometry for better compatibility with CAD viewers. **Edit model space first**; copied sheet linework will not automatically update. Rebuild/refresh sheet geometry as needed after model edits.

Dimension graphics are separate from walls and openings:

- `A-DIM-EXTERNAL-V52`: external wall-centerline annotations
- `A-DIM-CLEAR-V52`: internal horizontal clear annotations
- `A-DIM-CLEAR-VERTICAL-V53`: internal vertical clear annotations

Dimensions are currently **LINE/TEXT annotations, not associative DIMENSION objects**. Their text values will not update automatically when walls move. Keep dimension lines and text synchronized after edits.

This project uses **US English** drawing terminology. The original multi-cell A3 title-block geometry must remain unchanged in future revisions; update text only. No new banner-style title blocks.

## Files to keep in this repository

Suggested structure:

```text
Petaluma-House/
├── README.md
├── .gitignore
├── requirements.txt
├── drawings/
│   ├── Main_House_v60_All_Layouts_Fixed.dxf
│   └── Main_House_v60_Seven_Sheets.pdf
├── reference/
│   ├── master_bathroom_closet_sketch.svg
│   └── Main_House_v45_approved_baseline.dxf
├── scripts/
│   ├── export_sheets.py
│   └── check_dxf.py
└── docs/
    ├── drawing_conventions.md
    ├── revision_history.md
    └── validation_checklist.md
```

## Reproducing review exports

The scripts here are **newly reconstructed utilities**, not the historical scripts used to design revisions 45–60. The original authoring scripts were not available among the saved outputs. The archived approved v45 DXF is included under `reference/` for comparison; do not overwrite v60 with it. The current v60 DXF is the authoritative editable drawing. The export script generates a new review PDF and individual PNGs from that DXF; results can differ slightly in font metrics, plotting/color interpretation and other rendering details from the supplied reference PDF.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_dxf.py drawings/Main_House_v60_All_Layouts_Fixed.dxf
python scripts/export_sheets.py drawings/Main_House_v60_All_Layouts_Fixed.dxf --out build
```

For final plotted sheets, compare the exported pages with the versioned PDF and inspect in a CAD viewer. The exports are **not** an automatic geometry-authoring pipeline: they do not reconstruct the floor plan from the reference SVG.
