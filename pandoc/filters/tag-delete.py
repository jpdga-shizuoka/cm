#!/usr/bin/env python3
#
# タグ"=="で囲まれた文に打ち消し線を設定するためのフィルター
#
import panflute as pf
#
# Custom class for strikeouted text.
#
class Strikeout(pf.Inline):
    def __init__(self, *args):
        self._content = list(args)  # Strikeout内のコンテンツを保持

    def to_json(self):
        # Convert to JSON (required for custom Inline subclasses).
        return {
            "t": "Strikeout",
            "c": [child.to_json() for child in self._content]
        }

    @staticmethod
    def from_json(data):
        # Create an instance from JSON (required for custom Inline subclasses).
        content = [pf.load(element) for element in data['c']]
        return Strikeout(*content)

def action(elem, doc):
    if isinstance(elem, pf.Para) or isinstance(elem, pf.Plain):
        new_elems = []
        buffer = []  # Strikeout用のバッファ
        in_strikeout = False  # 現在Strikeout範囲内かどうかを判定

        for child in elem.content:
            if isinstance(child, pf.Str):
                text = child.text
                while text:
                    if in_strikeout:
                        # 終了タグを探す
                        end_tag_index = text.find('==')
                        if end_tag_index != -1:
                            # 終了タグが見つかった場合
                            buffer.append(pf.Str(text[:end_tag_index]))
                            new_elems.append(Strikeout(*buffer))
                            buffer = []
                            in_strikeout = False
                            # 残りのテキストを処理
                            text = text[end_tag_index + 2:]
                        else:
                            # 終了タグが見つからない場合
                            buffer.append(pf.Str(text))
                            text = ""
                    else:
                        # 開始タグを探す
                        start_tag_index = text.find('==')
                        if start_tag_index != -1:
                            # 開始タグが見つかった場合
                            if start_tag_index > 0:
                                new_elems.append(pf.Str(text[:start_tag_index]))
                            in_strikeout = True
                            text = text[start_tag_index + 2:]
                        else:
                            # 通常の文字列として追加
                            new_elems.append(pf.Str(text))
                            text = ""
            else:
                # Str以外の要素を処理
                if in_strikeout:
                    buffer.append(child)
                else:
                    new_elems.append(child)

        if in_strikeout:
            # 未終了のStrikeoutが残っている場合
            new_elems.append(Strikeout(*buffer))

        if isinstance(elem, pf.Para):
            return pf.Para(*new_elems)
        else:
            return pf.Plain(*new_elems)
#
# Add LaTeX definitions for custom strikeout class.
#
def prepare(doc):
    if doc.format == "latex":
        strikeout_latex = r"\newcommand{\Strikeout}[1]{\uline{#1}}"
        doc.metadata["header-includes"] = doc.metadata.get("header-includes", [])
        doc.metadata["header-includes"].append(pf.RawBlock(strikeout_latex, format="latex"))

def main(doc=None):
    return pf.run_filter(action, prepare=prepare, doc=doc)

if __name__ == "__main__":
    main()
