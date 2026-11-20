#!/usr/bin/env python3
"""Reconstructed v60 paper-space DXF exporter (not the historical authoring script).

Export every A3 paper-space layout directly from a canonical DXF to PNG and a
multipage PDF, using the paper-space linework in v60. Do not replace or edit the
source DXF. A3 landscape page coordinates are in millimeters (420 x 297).
"""
from pathlib import Path
import argparse
import ezdxf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.properties import LayoutProperties

PAGE_W, PAGE_H = 420, 297

def export(dxf_file: Path, out_dir: Path, dpi: int=180):
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = ezdxf.readfile(str(dxf_file))
    layouts = [layout for layout in doc.layouts if layout.name != 'Model']
    pdf_path = out_dir / 'drawings_from_dxf.pdf'
    with PdfPages(pdf_path) as pages:
        for layout in layouts:
            fig = plt.figure(figsize=(PAGE_W/25.4, PAGE_H/25.4), facecolor='white')
            ax = fig.add_axes((0, 0, 1, 1))
            ax.set_xlim(0, PAGE_W)
            ax.set_ylim(0, PAGE_H)
            ax.set_aspect('equal', adjustable='box')
            ax.set_axis_off()
            backend = MatplotlibBackend(ax, adjust_figure=False)
            props = LayoutProperties.from_layout(layout)
            props.set_colors(bg='#FFFFFF', fg='#000000')
            Frontend(RenderContext(doc), backend).draw_layout(layout, layout_properties=props)
            name = layout.name.split()[0]
            fig.savefig(out_dir/f'{name}.png', dpi=dpi, facecolor='white')
            pages.savefig(fig, facecolor='white')
            plt.close(fig)
            print('Exported', name)
    print('Wrote', pdf_path)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('dxf',type=Path)
    parser.add_argument('--out',type=Path,default=Path('build'))
    parser.add_argument('--dpi',type=int,default=180)
    args=parser.parse_args()
    export(args.dxf,args.out,args.dpi)
