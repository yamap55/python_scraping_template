"""ChromeDriver"""
import time
from logging import getLogger

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from python_scraping_test.config import (
    SELENIUM_MAX_GET_COUNT,
    SELENIUM_MAX_RETRIES,
    SELENIUM_RETRY_DELAY,
)

logger = getLogger(__name__)


class ManagedSeleniumDriver:
    """
    ChromeDriver

    ChromeDriverを毎回開くとかなりのコストがかかるため、使いまわしたいが以下の懸念がある。
    そのため、基本は使いまわしつつも時折再度生成するということを行う
    - セッションデータの蓄積
    - Seleniumの仕様上？エラーが発生しやすくなる
    """

    def __init__(self, timeout: int):
        """コンストラクタ"""
        self.timeout = timeout
        self.driver = None
        self.get_count = 0

    def _recreate_driver(self):
        if self.driver is not None:
            self.driver.close()
        self.driver = webdriver.Chrome(options=self._create_selenium_options())
        self.driver.set_page_load_timeout(self.timeout)
        self.get_count = 0

    def _create_selenium_options(self):
        options = Options()
        options.add_argument("--headless")  # ヘッドレスモードで実行
        options.add_argument("--no-sandbox")  # サンドボックスモードを無効化
        options.add_argument("--disable-gpu")  # GPUの使用を無効化
        options.add_argument("--disable-extensions")  # 拡張機能を無効化
        # ディスクキャッシュを無効化 コンテナ起動の場合は必須
        options.add_argument("--disable-dev-shm-usage")
        return options

    def get_driver(self) -> webdriver.Chrome:
        """ドライバーを取得する"""
        if self.driver is None or self.get_count >= SELENIUM_MAX_GET_COUNT:
            self._recreate_driver()
        return self.driver  # type: ignore

    def _get(self, url: str):
        self.get_driver().get(url)
        # 通常のWebDriverとは動きが異なるが、可読性が良いためsourceを返す
        return self.driver.page_source  # type: ignore

    def get(self, url: str):
        """ページを取得する"""
        self.get_count += 1

        for _ in range(SELENIUM_MAX_RETRIES):
            try:
                return self._get(url)
            except WebDriverException as e:
                logger.warning(f"Error occurred: {e}. Retrying...")
                time.sleep(SELENIUM_RETRY_DELAY)

        # 最後にdriverを作り直してから取得する
        self._recreate_driver()
        try:
            return self._get(url)
        except Exception as e:
            raise Exception("Failed to load the page after multiple attempts") from e

    def __enter__(self):
        """with構文用"""
        self._recreate_driver()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """with構文用"""
        if self.driver:
            self.driver.close()
