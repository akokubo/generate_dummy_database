# SQLiteデータベースのファイル名
DATABASE_FILE = "students.sqlite"

# データを投入するためのSQL文（テーブル「学生」へのINSERT文）
SQL = "INSERT INTO 学生 (名前, カナ, 誕生日, 学科) VALUES (?, ?, ?, ?)"

# 入力するデータが格納されているCSVファイルの名前
CSV_FILE = "students.csv"

# CSVファイルの文字コード設定
# Excelで保存された場合、通常は"shift_jis"だが、ここではutf-8としている
ENCODING = "utf-8"

# 必要なライブラリのインポート
import sqlite3
import csv

# SQLiteデータベースに接続
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

# CSVファイルを開く
with open(CSV_FILE, "r", encoding=ENCODING) as file:
    # CSVファイルを読み込む
    reader = csv.reader(file)
    
    # ヘッダーをスキップする（1行目はカラム名のため）
    next(reader)
    
    # CSVの各行に対して処理を行う
    for row in reader:
        # 各行に名前、カナ、誕生日、学科が含まれていることを確認
        if len(row) == 4:
            # SQL文を実行してデータをデータベースに挿入
            cursor.execute(SQL, row)

# 変更をデータベースにコミット（保存）
conn.commit()

# データベースの接続を閉じる
conn.close()
