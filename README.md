# Traial

## 環境変数の追加(.env)

manage.pyと同階層に.envファイルを作成する.
今回のプロジェクトの場合 作業ディレクトリ/mysite以下に作成する.
通常の環境変数(os.environ)とは違い、`environ`を利用する.
設定が必要な環境変数は以下の通り

・SECRET_KEY
・DEBUG
・ALLOWED_HOSTS
