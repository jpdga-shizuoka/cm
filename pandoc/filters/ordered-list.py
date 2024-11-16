#!/usr/bin/env python3
import panflute as pf
#
# 番号付きリストの記号を、PDGA形式に変更する
# see: https://scorreia.com/software/panflute/code.html#panflute.elements.OrderedList
#
STYLE_MAP = {
    0: 'UpperAlpha',  # A, B, C, ...
    1: 'Decimal',     # 1, 2, 3, ...
    2: 'LowerAlpha',  # a, b, c, ...
    3: 'LowerRoman'   # i, ii, iii, ...
}
#
# OrderedListのインデントレベル(ネストの深さ)を計算する
#
def get_indent_level(elem):
    level = 0
    parent = elem.parent
    while parent:
        if isinstance(parent, pf.OrderedList):
            level += 1
        parent = parent.parent
    return level
#
# OrderedListのインデントレベルに応じてstyleを書き換える
#
def find_def_labelenumi(elem, doc):
    if isinstance(elem, pf.OrderedList):
        level = get_indent_level(elem)
        # 対応するstyleを設定
        if level in STYLE_MAP:
            elem.style = STYLE_MAP[level]
        else:
            elem.style = 'Decimal'  # デフォルトスタイル
#
# フィルターのエントリーポイント
#
def main(doc=None):
    return pf.run_filter(find_def_labelenumi, doc=doc)

if __name__ == "__main__":
    main()
