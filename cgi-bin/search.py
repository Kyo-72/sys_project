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

        return rows


#ヒットした書籍を表示する

def print_hit_list(rows):
		
    if not rows:				# リストが空のとき
        print("そんな本はありません")
    else:
        for row in rows:
                info = ['ID','author','PUBLISHER','PRICE','ISBN']
                print("<p><table border= 1 >")
                print("<tr>")
                print("<th>TITLE</th>")
                print("<th>{}</th>".format(row['TITLE']))
                print("</tr>")
                
                for str in info:
                        print("<tr>")
                        print("<td>{}</td>".format(str))
                        print("<td>{}</td>".format(row[str]))
                        print("</tr>")
                print("</table></p>")
			
