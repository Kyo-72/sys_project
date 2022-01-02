import sqlite3
import os

db_path = "bookdb.db"	

#データベースを検索してヒットしたデータをリストで返す関数

def seach_books(str):
    	

        # データベースファイル名を指定
        con = sqlite3.connect(db_path)# データベースに接続
        con.row_factory = sqlite3.Row	# 属性名で値を取り出せるようにする
        cur = con.cursor()				# カーソルを取得

        try:
                # SQL文の実行
                input = str
                cur.execute("select * from BOOKLIST where TITLE like ? OR AUTHOR like ?", ('%' + input + '%','%' + input + '%'))
                rows =  cur.fetchall()		# 検索結果をリストとして取得

        except sqlite3.Error as e:
                # エラー処理
                print("Error occurred:", e.args[0])
                rows = []

        con.commit()
        con.close()
        type(rows)
        return rows


#ヒットした書籍を表示する


			
