#!/usr/bin/env python3
import panflute as pf
import sys

def wrap_with_latex(elem, doc):
    if isinstance(elem, pf.Div):
        sys.stderr.write(f"Detected Div: {elem}\n")
    return elem

def main(doc=None):
    pf.run_filter(wrap_with_latex, doc=doc)

if __name__ == "__main__":
    main()
