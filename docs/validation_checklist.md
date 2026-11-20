# Release checklist

Before publishing a revised DXF/PDF:

- [ ] Run `python scripts/check_dxf.py drawings/<version>.dxf`.
- [ ] Open **all seven paper-space tabs** in the target AutoCAD viewer and confirm content appears.
- [ ] Confirm sheet A-001 prints at 1:100 on A3; A-002 to A-005 at 1:75; A-007 at 1:100.
- [ ] Check every wall corner, stub and T-junction at high zoom; no exposed unclosed wall faces or doubled lines.
- [ ] Check window edges and wall end caps: black wall terminations; no obsolete wall centerline crossing glazing.
- [ ] Confirm bedroom, bathroom and closet labels are within the appropriate clear space.
- [ ] Check all dimension text against overlapping walls, labels, windows, swings and other dimensions.
- [ ] Confirm external centerline spans and internal clear widths/depths agree with DXF endpoints.
- [ ] Check paper-space title block and spelling on every sheet.
- [ ] Render each sheet, compare with prior revision, and review at intended print size.
- [ ] Include the PDF and editable DXF from the same revision in the Git commit.

**Limit:** A successful CAD audit checks file validity, not wall-joining aesthetics or correctness of measured site conditions.
