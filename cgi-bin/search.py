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
                title = str
                cur.execute("select * from BOOKLIST where TITLE like ? ", ('%' + title + '%',))
                rows =  cur.fetchall()		# 検索結果をリストとして取得

        except sqlite3.Error as e:
                print(os.getcwd())# エラー処理
                print("Error occurred:", e.args[0])
                rows = []

        con.commit()
        con.close()

        return rows


#ヒットした書籍を表示する

def print_hit_list(rows):
		
	if not rows:				# リストが空のとき
		print("そんな本はありません")
	else:
		for row in rows:		# 検索結果を1つずつ処理
			print("<p>ID = %s</p>" % str(row['ID']))
			print("<br>タイトル = %s</br>" % str(row['TITLE']))
			print("<br>著者 = %s</br>" % str(row['author']))
			print("<br>出版社 = %s</br>" % str(row['PUBLISHER']))
			print("<br>価格 = %s</br>" % str(row['PRICE']))
			print("<br>ISBN = %s</br>" % str(row['ISBN']))
			print("<br>-------</p>")
