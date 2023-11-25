"""CSVを書き込むためのライター"""
import csv
from logging import getLogger
from pathlib import Path

logger = getLogger(__name__)


class ManagedCsvWriter:
    """
    CSVを書き込むためのライター

    リファクタリングという特性上、以下の懸念があるため定期的にファイルを開きなおすことを行う
    - 途中で落ちた際にデータを失いたくないこと
    - 実行時間が長いためファイルが長期間開きっぱなしになること
    """

    def __init__(self, output_path: Path, max_write_count=100):
        """コンストラクタ"""
        self.output_path = output_path
        self.max_write_count = max_write_count
        self.file = None
        self.writer = None
        self.write_count = 0

    def _reopen_file(self):
        if self.file is not None:
            self.file.close()
        self.file = open(self.output_path, "a", newline="", encoding="utf-8")
        self.writer = csv.writer(
            self.file,
            delimiter=",",  # 区切り文字はカンマ
            quotechar='"',  # 囲い文字はダブルクォーテーション
            quoting=csv.QUOTE_NONNUMERIC,
        )
        self.write_count = 0

    def get_writer(self) -> csv.writer:  # type: ignore
        """ライターを取得する"""
        if self.writer is None or self.write_count >= self.max_write_count:
            self._reopen_file()
        return self.writer

    def writerow(self, data):
        """データを書き込む"""
        self.get_writer().writerow(data)
        self.file.flush()  # 確実に書き込むためにflushする # type: ignore
        self.write_count += 1

    def __enter__(self):
        """with構文用"""
        self._reopen_file()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """with構文用"""
        if self.file:
            self.file.close()
