from time import  sleep
from selenium import  webdriver
#实例化一个浏览器
chrome = webdriver.Chrome()
#获取页面
chrome.get("https://read.qidian.com/chapter/6iBNYL2lFU0WXXlYBroA6g2/0VKc_lGiebjwrjbX3WA1AA2")
p_bookname = chrome.find_element_by_xpath('//div[@class="book-cover-wrap"]/h1')
with open(p_bookname.text + '.txt', 'a', encoding='utf-8') as b:
    b.write("小说")
def getFile(url):
    # # 实例化一个浏览器
    chrome = webdriver.Chrome()
    #获取页面
    chrome.get(url)
    #捕获元素
    p_list = chrome.find_elements_by_xpath('//div[@class="read-content j_readContent"]/p')
    p_zhangming = chrome.find_element_by_xpath('//div[@class="text-head"]/h3')
    with open(p_bookname.text+'.txt','a',encoding='utf-8') as b:
        b.write(p_zhangming.text+'\n')
    for p in p_list:
        with open(p_bookname.text+'.txt','a',encoding='utf-8') as a:
             a.write(p.text+'\n')
    next_url = chrome.find_element_by_xpath('//div[@class="chapter-control dib-wrap"]/a[@id="j_chapterNext"]')
    if next_url:
        next_urls = next_url.get_attribute("href")
        print(next_urls)
        chrome.close()
        getFile(next_urls)
    else:
        chrome.close()
        return

getFile("https://read.qidian.com/chapter/6iBNYL2lFU0WXXlYBroA6g2/0VKc_lGiebjwrjbX3WA1AA2")