#!/usr/bin/env python3
#
# `++`マークアップ記号を削除する
#
import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Str):
        # テキストから`++`を削除
        elem.text = elem.text.replace("++", "")
    return elem

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
