簡単な起動方法
ターミナル(WIndowsはコマンドプロンプト)にて
cdコマンドでsample_app配下に移動
以下コマンドを実行
python run.py
ブラウザ(chrome、safari等)で
(port番号は他と競合しないため、わざと5099にしています)
http://localhost:5099/
http://127.0.0.1:5099/
にアクセスするとトップページ画面
templates/index.htmlの画面が表示される

ソースコードの内容説明
app/run.py
→アプリケーションの開発サーバーを起動するためのファイル

app/static/style.css
→templates/index.htmlのcssファイル

app/templates/index.html
→http://localhost:5099/で表示されるページ

app/__init__.py
→DB関連、現在sqliteなので、docker起動して、今後はpostgresに接続するように対応

app/databese.py
→__init__.pyで読み込み元のファイル、__init__.pyと統一しても良いが後ほどリファクタリングの時に検討する。

app/models.py
→モデルのファイル、従業員の一覧のためのテーブル

app/routes.py
→エンドポイント(API一覧)のファイル

schemas.py
→レスポンスの戻り値関連のファイル
