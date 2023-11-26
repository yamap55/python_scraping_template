"""ユーザー情報を格納する"""

from dataclasses import dataclass, fields


@dataclass
class User:
    """ユーザー情報を格納する"""

    user_id: str
    user_name: str
    age: str

    @staticmethod
    def get_headers():
        """CSV出力する際のヘッダーを取得する"""
        return [f.name for f in fields(User)]

    def to_csv_row(self):
        """CSV出力する際の行データを取得する"""
        return [getattr(self, f.name) for f in fields(self)]
