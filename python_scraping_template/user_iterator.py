"""ユーザーを一覧から順に取得する"""

from logging import getLogger
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from python_scraping_template.config import (
    BASE_URL,
)

logger = getLogger(__name__)


class UserIterator:
    """
    ユーザーを一覧から順に取得する
    """

    def __init__(self, max_page=1):
        """
        コンストラクタ

        Parameters
        ----------
        max_page : int, optional
            最大ページ（このページまで一覧を探索する）, by default 1
        """
        self.users = []
        self.page = 1
        self.max_page = max_page
        # 一覧ページは1ページに3ユーザー存在する
        self.max_user_count = max_page * 3
        self.index = 0

    def __iter__(self):
        """イテレータ"""
        return self

    def __next__(self):
        """次のユーザーを取得する"""
        self.index = self.index + 1
        if not self.users and self.page <= self.max_page:
            self.load_users()

        if not self.users:
            raise StopIteration

        logger.info(f"{self.index} / {self.max_user_count}")
        return self.users.pop(0)

    def _get_users(self, page=1):
        full_url = urljoin(BASE_URL, f"/python_scraping_template/users/{page}.html")
        logger.info(f"Loading {full_url}")
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, "html.parser")

        user_table = soup.find("table")
        users = [tr for tr in user_table.find_all("tr") if tr.find_all("td")]  # type: ignore
        return users

    def load_users(self):
        """一覧ページを読み込み、ユーザーを取得する"""
        try:
            new_users = self._get_users(page=self.page)
            self.users.extend(new_users)
            self.page += 1
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise Exception("load_users failed") from e
