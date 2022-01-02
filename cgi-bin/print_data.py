def print_hit_list(rows,url_list):
    		
    if not rows:				# リストが空のとき
        print("そんな本はありません")
    else:
        for i,row in enumerate(rows):
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
                #最後にurlを張る
                print("<a href={}>{} </a>".format(url_list[i],row["TITLE"]) )
                
                