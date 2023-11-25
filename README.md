# python_scraping_test

本リポジトリは Python でスクレイピングを試すリポジトリです

## 環境詳細

- Python : 3.11

### 開発手順

1. VS Code 起動
2. 左下のアイコンクリック
3. 「Dev Containers: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナー image の取得や作成が行われる
5. 起動したら開発可能

## 事前準備

- `python_scraping_test/config.py` の内容を更新

## 実行方法

`python main.py`

※ `output/{yyyyMMddhhmmss}/output.csv` に結果が出力される

## memo

- Chrome 自体の動作確認
  - `google-chrome --no-sandbox --headless --disable-gpu --screenshot="screenshot_$(date +"%Y%m%d").png" --window-size=1280,1080 https://www.ugtop.com/spill.shtml`
- Chrome のバージョン確認
  - `google-chrome --version`
- WebDriver for Chrome のバージョン確認
  - `poetry show | grep chromedriver-binary`
