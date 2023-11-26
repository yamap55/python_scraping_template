"""汎用関数"""
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
