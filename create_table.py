# SQLiteデータベースのファイル名
DATABASE_FILE = "students.sqlite"

# 学生テーブルを作成するためのSQL文
SQL = """
CREATE TABLE IF NOT EXISTS 学生 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  # 主キー（自動増分）
    名前 VARCHAR NOT NULL,                 # 名前（必須）
    カナ VARCHAR NOT NULL,                 # カナ（必須）
    誕生日 DATE,                          # 誕生日（日付形式）
    学科 VARCHAR                          # 学科（任意）
)
"""

# sqlite3モジュールをインポート
import sqlite3

# データベースに接続（指定したファイルがなければ新しく作成される）
# ここで作成するのは、学生データを格納するためのSQLiteデータベース
conn = sqlite3.connect(DATABASE_FILE)

# データベース操作を行うためのカーソルを取得
cursor = conn.cursor()

# テーブルを作成するSQL文を実行
# `IF NOT EXISTS`を使用することで、既にテーブルが存在する場合はエラーにならずにスキップされます
cursor.execute(SQL)

# 変更をデータベースに保存
# SQL文による変更は、コミットしないと実際にデータベースに反映されません
conn.commit()

# データベースとの接続を閉じる
# 作業が終わったら接続を閉じることが良い習慣です
conn.close()

# このプログラムを実行すると、"students.sqlite"というファイルに学生テーブルが作成される
