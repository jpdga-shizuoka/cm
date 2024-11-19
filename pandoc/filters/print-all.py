#!/usr/bin/env python3
#
# すべての要素をプリント出力するためのフィルター
#
import panflute as pf

def debug_all_elements(elem, doc):
    pf.debug(f"Element: {type(elem)} - {elem}")
    return elem

def main(doc=None):
    pf.run_filter(debug_all_elements, doc=doc)

if __name__ == "__main__":
    main()
