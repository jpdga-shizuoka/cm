#!/usr/bin/env python3
#
# タグ"++"で囲まれた文に下線を設定するためのフィルター
#
import panflute as pf
#
# Inlineクラスを継承し下線クラスを作成する
# 
class Underline(pf.Inline):
    def __init__(self, *args):
        self._content = list(args)  # Underline内のコンテンツを保持

    # Convert to JSON (required for custom Inline subclasses).
    def to_json(self):
        return {
            "t": "Underline",
            "c": [child.to_json() for child in self._content]
        }

    @staticmethod
    def from_json(data):
        # Create an instance from JSON (required for custom Inline subclasses).
        content = [pf.load(element) for element in data['c']]
        return Underline(*content)

def action(elem, doc):
    if isinstance(elem, pf.Para) or isinstance(elem, pf.Plain):
        new_elems = []
        buffer = []  # Underline用のバッファ
        in_underline = False  # 現在Underline範囲内かどうかを判定

        for child in elem.content:
            if isinstance(child, pf.Str):
                # `++`タグを探す
                if in_underline:
                    # 終了タグを探す
                    end_tag_index = child.text.find('++')
                    if end_tag_index != -1:
                        # 終了タグが見つかった場合
                        buffer.append(pf.Str(child.text[:end_tag_index]))
                        new_elems.append(Underline(*buffer))
                        buffer = []
                        in_underline = False
                        # 残りのテキストを処理
                        remainder = child.text[end_tag_index + 2:]
                        if remainder:
                            new_elems.append(pf.Str(remainder))
                    else:
                        # 終了タグが見つからない場合、全体をバッファに追加
                        buffer.append(child)
                else:
                    # 開始タグを探す
                    start_tag_index = child.text.find('++')
                    if start_tag_index != -1:
                        # 開始タグが見つかった場合
                        new_elems.append(pf.Str(child.text[:start_tag_index]))
                        in_underline = True
                        buffer.append(pf.Str(child.text[start_tag_index + 2:]))
                    else:
                        # 通常の文字列として追加
                        new_elems.append(child)
            else:
                # Str以外の要素を処理
                if in_underline:
                    buffer.append(child)
                else:
                    new_elems.append(child)

        if in_underline:
            # 未終了のUnderlineが残っている場合
            new_elems.append(Underline(*buffer))

        if isinstance(elem, pf.Para):
            return pf.Para(*new_elems)
        else:
            return pf.Plain(*new_elems)
#
# Add LaTeX definitions for custom underline class.
#
def prepare(doc):
    if doc.format == "latex":
        underline_latex = r"\newcommand{\Underline}[1]{\uline{#1}}"
        doc.metadata["header-includes"] = doc.metadata.get("header-includes", [])
        doc.metadata["header-includes"].append(pf.RawBlock(underline_latex, format="latex"))

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, doc=doc)

if __name__ == "__main__":
    main()
