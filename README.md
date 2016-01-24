# Django_login_logout_sample

## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_login_logout_sample.git

# virtualenv環境の作成とactivate
# *Python3.5は、`c:\python35-32\`の下にインストール
path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# マイグレーション
(env)path\to\dir>python manage.py migrate

# 開発サーバの起動
(env)path\to\dir>python manage.py runserver

# 開発サーバのURLを既定のブラウザで開く
# (別のコマンドプロンプトを開いて実行)
>start http://localhost:8000/mysite/user-creation
>start http://localhost:8000/mysite/<user_id>/update
>start http://localhost:8000/mysite/login
>start http://localhost:8000/mysite/logout-with-template
>start http://localhost:8000/mysite/logout-with-redirect
>start http://localhost:8000/mysite/logout-then-login
>start http://localhost:8000/mysite/password-change
>start http://localhost:8000/mysite/password-reset
```

　  
## テスト環境

- Windows10
- Python 3.5.1
- Django 1.9.1

　  
## 関係するブログ

- [Djangoで、Djangoアプリ単体でのユーザ作成・変更・認証・パスワード変更・パスワードリセットを試してみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/01/24/223846)