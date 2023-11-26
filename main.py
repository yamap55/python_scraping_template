"""main"""
import time
from logging import config, getLogger
from time import perf_counter
from urllib.parse import urljoin

from python_scraping_template.config import (
    BASE_OUTPUT_PATH,
    BASE_URL,
    SCRAPING_END_PAGE,
    SCRAPING_TRANSITION_PAUSE,
    SELENIUM_TIMEOUT,
)
from python_scraping_template.managed_csv_writer import ManagedCsvWriter
from python_scraping_template.managed_selenium_driver import ManagedSeleniumDriver
from python_scraping_template.user import User
from python_scraping_template.user_detail import UserDetail
from python_scraping_template.user_iterator import UserIterator
from python_scraping_template.util import create_output_directory, simple_format_time

config.fileConfig("logging.conf", disable_existing_loggers=False)

logger = getLogger(__name__)


def append_data(user, writer: ManagedCsvWriter, driver: ManagedSeleniumDriver):
    """ユーザーのデータを取得してCSVに書き込む"""
    user_url = user.find("a").get("href")
    user_full_url = urljoin(BASE_URL, user_url)

    user_detail_data = UserDetail(user_full_url, driver).get_user_data()
    user = User(
        **user_detail_data,
    )
    writer.writerow(user.to_csv_row())


def main():
    """main"""
    logger.info("Start scraping")
    output_dir_path = create_output_directory(BASE_OUTPUT_PATH)
    logger.info(f"Output directory: {output_dir_path}")

    output_path = output_dir_path / "output.csv"
    header = User.get_headers()

    with ManagedCsvWriter(output_path) as writer:
        writer.writerow(header)  # ヘッダの書き込み
        with ManagedSeleniumDriver(SELENIUM_TIMEOUT) as driver:
            for user in UserIterator(SCRAPING_END_PAGE):
                try:
                    append_data(user, writer, driver)
                except Exception:
                    # 予期せぬページが登場して失敗することがある
                    # 途中で止まってほしくないためエラー出力してその次のページへ進む
                    logger.error(f"Failed append data. {user}")
                time.sleep(SCRAPING_TRANSITION_PAUSE)
    logger.info(f"End scraping. output: {output_dir_path}")


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    elapsed_time = f"{(end-start)/60:.2f}"
    logger.info(f"経過時間: {simple_format_time(elapsed_time)}")
