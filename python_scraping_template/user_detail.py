"""ユーザー詳細ページの情報"""
from logging import getLogger

from bs4 import BeautifulSoup

from python_scraping_template.managed_selenium_driver import ManagedSeleniumDriver

logger = getLogger(__name__)


class UserDetail:
    """ユーザー詳細ページの情報"""

    def __init__(self, user_full_url: str, driver: ManagedSeleniumDriver) -> None:
        """コンストラクタ"""
        logger.info(f"Loading {user_full_url}")
        html = driver.get(user_full_url)
        self.soup = BeautifulSoup(html, "html.parser")

    def get_user_data(self):
        """ユーザー詳細ページの情報を取得する"""
        user_details = self.soup.find("div", class_="user-details")
        user_data_list = user_details.find_all("span", class_="value")  # type: ignore
        [user_id, user_name, user_age] = [value.text for value in user_data_list]
        return {
            "user_id": user_id,
            "user_name": user_name,
            "age": user_age,
        }
