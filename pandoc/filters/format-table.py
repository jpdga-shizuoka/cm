#!/usr/bin/env python3
#
# 表の書式を変更するフィルター
#
import panflute as pf
#
# 表の文字を小さくかつ行間をさらに狭めたい表は、
# そのキャプションを下記リストに登録する
#
SMALLER_TABLE_LIST = [
    "ティアの基準(北米限定)",
    "ティアの基準(北米以外の大会)"
]
# 上のりストにヒットした表は、以下を適用する
SMALLER_TABLE_FORMAT = r"\footnotesize\renewcommand{\arraystretch}{0.6}"
# それ以外の表は、以下を適用する
STANDARD_TABLE_FORMAT = r"\renewcommand{\arraystretch}{0.8}"
#
# 指定された要素に指定されたlatexを追加し、それをグループで包み、返す
#
def wrap_with(elem, latex):
    begin_latex = r"\begingroup" + latex
    end_latex = r"\endgroup"
    wrapped_content = [
        pf.RawBlock(begin_latex, format="latex"),
        elem,
        pf.RawBlock(end_latex, format="latex")
    ]
    return wrapped_content
#
# Table要素を見つける毎に、
# Captionの有無、登録リストに一致するかを確認し、
# 追加する書式を変えて、新しく作った要素を返す
#
def action(elem, doc):
    if isinstance(elem, pf.Table):
        # pf.debug(f"Element: {type(elem)}")
        caption = elem.caption
        if caption:
            caption_text = pf.stringify(caption)
            if caption_text in SMALLER_TABLE_LIST:
                # リストに登録されたCaption
                return wrap_with(elem, SMALLER_TABLE_FORMAT)
            else:
                # リストに登録されていないCaption
                return wrap_with(elem, STANDARD_TABLE_FORMAT)
        else:
            # Caption無しTable
            return wrap_with(elem, STANDARD_TABLE_FORMAT)
    # Table以外は素通り
    return elem

def main(doc=None):
    pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()
