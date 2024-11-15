#!/usr/bin/env python3
import panflute as pf
import sys
import re

def detect_and_convert_fenced_divs(elem, doc):
    """
    リスト内の`::: bigwidetable`を検出し、特別なLaTeX書式でラップ。
    """
    if isinstance(elem, pf.Para):
        # `Para`内に`::: bigwidetable`があるか検出
        text = pf.stringify(elem)
        if re.search(r"^:{3,}\s*bigwidetable", text):
            sys.stderr.write(f"Detected inline fenced div in Para: {text}\n")

            # `Table`が次の要素として存在するか確認
            next_elem = elem.next
            if isinstance(next_elem, pf.Table):
                sys.stderr.write("Found associated Table after fenced div\n")
                div_start = pf.RawBlock(r"\begingroup\footnotesize\renewcommand{\arraystretch}{0.8}", format="latex")
                return div_start

        elif re.search(r"^:{3,}\s*$", text):
            sys.stderr.write(f"Removing Para with text: {text}\n")
            div_end = pf.RawBlock(r"\endgroup", format="latex")
            return div_end

    elif isinstance(elem, pf.Div) and "bigwidetable" in elem.classes:
        # 正常に`Div`として認識される場合
        sys.stderr.write(f"Detected valid Div: {elem}\n")
        return wrap_as_latex(elem)

    return elem

def wrap_as_latex(elem):
    """
    `bigwidetable`クラスを持つDiv要素をLaTeXのコードでラップ。
    """
    begin_latex = r"\begingroup\footnotesize\renewcommand{\arraystretch}{0.8}"
    end_latex = r"\endgroup"
    wrapped_content = [
        pf.RawBlock(begin_latex, format="latex"),
        *elem.content,
        pf.RawBlock(end_latex, format="latex"),
    ]
    return pf.Div(*wrapped_content, classes=elem.classes)

def main(doc=None):
    """
    Pandocフィルタのメイン処理。
    """
    sys.stderr.write("Starting filter...\n")
    pf.run_filter(detect_and_convert_fenced_divs, doc=doc)
    sys.stderr.write("Filter finished.\n")

if __name__ == "__main__":
    main()
