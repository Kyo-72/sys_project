#! /usr/bin/env python

import sys
import io
import cgi
import search

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
param_str = form.getvalue('param1','')



print("Content-type: text/html")
print("")
print("<html>")
print(" <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print(" <body>")
#データベースから文字列を検索して、一致する書籍情報を取得
book_info = search.seach_books(param_str)
search.print_hit_list(book_info)
print(" </body>")
print("</html>")
