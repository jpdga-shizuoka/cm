#!/usr/bin/env python3
import panflute as pf
import sys

def debug_all_elements(elem, doc):
    """
    すべての要素をデバッグ出力。
    """
    sys.stderr.write(f"Element: {type(elem)} - {elem}\n")
    return elem

def main(doc=None):
    """
    メイン処理。
    """
    sys.stderr.write("Starting debug...\n")
    pf.run_filter(debug_all_elements, doc=doc)
    sys.stderr.write("Finished debug.\n")

if __name__ == "__main__":
    main()
