"""設定値"""
from pathlib import Path

BASE_URL = "https://yamap55.github.io/"
BASE_OUTPUT_PATH = Path("./output")
SELENIUM_MAX_RETRIES = 5  # SELENIUMでエラーになった際に最大何回リトライするか
SELENIUM_RETRY_DELAY = 5  # SELENIUMでエラーになった際に何秒待ってからリトライするか（単位は秒）
SELENIUM_TIMEOUT = 30  # SELENIUMの最大待ち時間（単位は秒）
SELENIUM_MAX_GET_COUNT = 20  # SELENIUMで何回getしたら再生成するか
SCRAPING_TRANSITION_PAUSE = 1  # データを取得する際の待ち時間
SCRAPING_END_PAGE = 3
