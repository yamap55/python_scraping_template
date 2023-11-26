# python_scraping_template

本リポジトリは Python でスクレイピングを試すためのテンプレートリポジトリです
devcontainer の設定をしていますので、VS Code と Docker、Git さえあれば各種開発用設定が行われた Python の開発環境が構築され、即時開発が可能です
GitHub のリポジトリページの「Use this template」を押下して使用してください

## 内容

- [devcontainer](https://code.visualstudio.com/docs/remote/containers)
- lint
  - [ruff](https://beta.ruff.rs/docs/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), [pyright](https://github.com/microsoft/pyright)
  - [hadolint](https://github.com/hadolint/hadolint)
- [poetry](https://python-poetry.org/)
- [GitHub Actions](https://github.co.jp/features/actions)
- [logging](https://docs.python.org/ja/3/howto/logging.html)

## 環境詳細

- Python : 3.11

### 事前準備

- Docker インストール
- VS Code インストール
- VS Code の拡張機能「Remote - Containers」インストール
  - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
- 本リポジトリの clone
- ssh-agent の設定
  - https://code.visualstudio.com/docs/devcontainers/containers#_using-a-credential-helper
- 以下をプロジェクト名に合わせて変更
  - `.devcontainer/devcontainer.json`
    - `name`, `service`
  - `compose.yaml`
    - `services` の Key 名
    - `image`, `container_name`
    - `env_file`
      - 環境変数を使用しない場合は除去
  - main.py
  - logging.conf
    - `hoge` を使用するモジュール名に合わせる
  - `README.md`
  - `LICENSE`
  - dependabot
    - `.github/dependabot.yml`
    - `.github/workflows/auto_merge_depandabot.yml`
  - pyproject.toml
    - `tool.poetry.name`, `tool.poetry.description`, `tool.poetry.authors`
- Chrome、Webdriver のバージョン変更
  - 使用時のバージョンに合わせて以下のバージョンを更新してください
  - Chrome
    - 確認: https://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-chrome-stable
    - 変更: `.devcontainer/Dockerfile`
  - Webdriver
    - 確認: https://pypi.org/project/chromedriver-binary/
    - 変更: `pyproject.toml`

### 開発手順

1. VS Code 起動
2. 左下のアイコンクリック
3. 「Dev Containers: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナー image の取得や作成が行われる
5. 起動したら開発可能

## 事前準備

- `python_scraping_template/config.py` の内容を更新

## 実行方法

`python main.py`

## サンプルコード説明

- サンプルコードを実行すると以下のサンプルページの情報を取得して CSV を出力します
  - `https://yamap55.github.io/python_scraping_template/users/1.html`
  - 出力先: `output/{yyyyMMddhhmmss}/output.csv`
- 一覧は静的サイトを想定して requests、詳細ページは動的ページを想定して Selenium で取得しています

## memo

- Chrome 自体の動作確認
  - `google-chrome --no-sandbox --headless --disable-gpu --screenshot="screenshot_$(date +"%Y%m%d").png" --window-size=1280,1080 https://www.ugtop.com/spill.shtml`
- Chrome のバージョン確認
  - `google-chrome --version`
- WebDriver for Chrome のバージョン確認
  - `poetry show | grep chromedriver-binary`
