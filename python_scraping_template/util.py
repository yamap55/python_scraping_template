"""汎用関数"""

import re
from datetime import datetime
from pathlib import Path


def simple_format_time(duration):
    """
    秒数をHH時間MM分SS秒にフォーマットする
    """
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}時間{int(minutes)}分{int(seconds)}秒"


def create_output_directory(base_output_path: Path) -> Path:
    """
    指定したパスの配下に出力ディレクトリを作成

    出力ディレクトリはYYYYMMDDHHMMSS形式
    中間ディレクトリは自動で作成される
    """
    datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = base_output_path / datetime_str
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def parse_numbers_from_text(text: str) -> str:
    """
    与えられたテキスト文字列から数値を抽出し、それらを連結した文字列として返す。

    テキスト内の任意の位置にある全ての数値（整数および浮動小数点数）を識別し、
    それらを発見した順に連結した単一の文字列を生成します。数値以外の文字は無視されます。

    Examples
    --------
    - 入力: "現在の支援総額12,345,678円"
      出力: "12345678"
    - 入力: "この部屋には10個の椅子と20個のテーブルがあります。"
      出力: "1020"
    - 入力: "合計で2.5時間かかりました。"
      出力: "2.5"

    注意: この関数は数値を抽出して連結するだけであり、抽出された数値間に区切り文字は挿入しません。
    """
    numbers = re.findall(r"\d+\.?\d*", text)
    return "".join(numbers)
