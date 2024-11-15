#!/usr/bin/env python3
#
# `ordg/`は、`https://jpdga-shizuoka.github.io/rules/`に
# `dgj/`は、`https://jpdga-shizuoka.github.io/ssa-round-ratings/libraries/`に
# 置き換えるフィルター
# 
import panflute as pf

def replace_urls(elem, doc):
    if isinstance(elem, pf.Link):
        # 元のURLを取得
        url = elem.url
        # URLの置き換え
        if url.startswith("ordg/"):
            elem.url = url.replace("ordg/", "https://jpdga-shizuoka.github.io/rules/")
        elif url.startswith("dgj/"):
            elem.url = url.replace("dgj/", "https://jpdga-shizuoka.github.io/ssa-round-ratings/libraries/")
    return elem

def main(doc=None):
    return pf.run_filter(replace_urls, doc=doc)

if __name__ == "__main__":
    main()
