from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests
import re
from bs4 import BeautifulSoup

def search_for_url(isbn):

    # chromedriverの設定
    options = Options() 
    options.add_argument('--headless')
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    #urlからブラウザを開く
    url = "https://www.kinokuniya.co.jp/"
    browser.get(url)
    # 待機時間を設定
    browser.implicitly_wait(5)
    
    # #検索画面に文字列を送る
    elem_search_form = browser.find_element_by_class_name("search_text")
    elem_search_form.send_keys(isbn)
    #検索ボタンを押す
    elem_send_btn = browser.find_element_by_class_name("submit2")
    elem_send_btn.click()
    #beautifull soupでhtml解析する。まずは準備
    html = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    try:
        elem_book = soup.find('div',attrs={'id':'main_contents'})
        elem_book = elem_book.find('form',attrs={'name':'listForm'})
        elem_book = elem_book.find('div',attrs={'class':'list_area_wrap'})
        #class 検索結果一覧の子要素をすべて取る
        elem_book = elem_book.contents
        book_list = []
        #改行文字の処理
        for i in range(len(elem_book)):
            if(i % 2 != 0):
                book_list.append(elem_book[i])
        len(book_list)
        
    except AttributeError:
        return "NON_RESULT"

    #書籍購入ページへのurlを取得
    if( len(book_list) != 1):
        print("検索結果が正しくない可能性あり.ヒット数:{}".format(len(book_list)))

    url = book_list[0].find('h3',attrs={'class':'heightLine-2'})
    url = url.find("a")
    url = url.get("href")

    browser.quit()

    return url

def search_for_url_list(book_info):
    url_list = []
    for b in book_info:
        isbn = b["ISBN"]
        url_list.append(search_for_url(isbn))

    return url_list 