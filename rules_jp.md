# MCPコマンド（Selenium）

このプロジェクトのMCPサーバーで使用できるコマンド（ツール）の一覧です。

## 使用可能なコマンド
- `open_browser(start_url)`
  - ブラウザを開き、`start_url`へ移動します。既定値: `about:blank`
- `navigate(url)`
  - 現在のブラウザで指定した`url`へ移動します。
- `click(css=None, xpath=None, timeout_sec=10)`
  - 指定した要素をクリックします。`css`または`xpath`のいずれかが必須です。
- `type_text(text, css=None, xpath=None, clear_first=True, timeout_sec=10)`
  - 指定した入力要素にテキストを入力します。`css`または`xpath`のいずれかが必須です。
- `get_text(css=None, xpath=None, timeout_sec=10)`
  - 指定した要素のテキストを取得します。`css`または`xpath`のいずれかが必須です。
- `get_page_source()`
  - 現在のページのHTMLソースを返します。
- `screenshot(path)`
  - 現在の画面を`path`にスクリーンショットとして保存します。
- `close_browser()`
  - ブラウザを終了します。

## 簡単な例
- `open_browser("https://www.example.com")`
- `click(css="#login")`
- `type_text("hello", css="input[name='q']")`
- `get_page_source()`

## 運用ルール
- 新しく追加するmdファイルは常にUTF-8で保存する。
- 特定のサイトを呼び出す場合は、`{site}-{YYYYMMDD}.md`を先に読み、その指示に従う。
- サイト探索前にスクリーンショットを保存し、画面を理解してから一般的なブラウザの開発者ツールの流れでDOM探索を行う。
- 全HTMLを無条件で取得せず、必要なときのみ`get_page_source()`を使用する。
- Webを読むときはスクリーンショットで頻繁に確認して素早く探索し、画像ベースのUI（ボタン等）でHTMLだけでは理解しにくい場合に備える。
- Web探索作業後は再現可能な「完全記録」形式のmdを残す。
  - 各ステップは`action + selector + 結果`を1行で記録する。
  - selectorはcss/xpathをそのまま残し、成功/timeoutなどの結果を明記する。
  - 必要に応じて繰り返し回数（xN）と範囲（[i..j]）を記載する。
  - PC依存情報（絶対パス、ユーザー名など）は記録しない。
