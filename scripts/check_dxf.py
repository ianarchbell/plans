#!/usr/bin/env python3
"""Basic v60 CAD sanity checks. Geometry appearance still needs visual review."""
import argparse
import collections
import ezdxf

EXPECTED = ['A-001 A3','A-002 A3','A-003 A3','A-004 A3','A-005 A3','A-006 A3','A-007 A3']
DIM_LAYERS = ('A-DIM-EXTERNAL-V52', 'A-DIM-CLEAR-V52', 'A-DIM-CLEAR-VERTICAL-V53')

def main(path):
    doc=ezdxf.readfile(path)
    audit=doc.audit()
    assert not audit.errors, f'{len(audit.errors)} DXF audit errors'
    assert all(name in doc.layout_names() for name in EXPECTED), 'Missing sheet layout'
    for name in EXPECTED:
        lay=doc.layouts.get(name)
        print(name, 'entities:',len(lay),'dimension entities:',sum(e.dxf.layer in DIM_LAYERS for e in lay))
        assert len(lay)>50, f'Almost empty sheet: {name}'
    print('Model-space dimension layers:')
    ct=collections.Counter(e.dxf.layer for e in doc.modelspace())
    for layer in DIM_LAYERS:
        print(' ',layer,ct[layer])
        assert ct[layer]>0, f'Missing {layer}'
    assert sum(e.dxf.layer in DIM_LAYERS for e in doc.layouts.get('A-007 A3'))>100,'A-007 not fully dimensioned'
    print('DXF audit and presence checks passed. Visual check still required.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('dxf');main(p.parse_args().dxf)
