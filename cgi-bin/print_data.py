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