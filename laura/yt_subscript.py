# 載入需要的套件
from selenium import webdriver
# import requests
import csv
from selenium.webdriver.common.by import By

channels=[]
with open(r'C:\Users\GOOD\Desktop\碩班\110-1\IM\final project\ytr_crawl.csv', "r", encoding="utf-8 sig") as f:
    rows = f.read().lower().split('\n')
    for row in rows:
        if row == '':
            continue
        else:
            channels.append(row.split(',')[0])
    f.close()
print(channels)


# 開啟瀏覽器視窗(Chrome)
# 方法二：或是直接指定exe檔案路徑
subscribe_list=[]
driver = webdriver.Chrome(r'C:\Users\GOOD\Desktop\chromedriver.exe')

with open('subscribe_list.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'subscriberCount'])
    for channel in channels:
        driver.get("https://www.youtube.com/results?search_query="+channel) # 更改網址以前往不同網頁
        # # 定位搜尋框
        # element = driver.find_element_by_xpath("//input[@id='search']")
        # # 傳入字串
        # element.send_keys('阿滴英文')
        # button = driver.find_element_by_xpath("//ytd-searchbox/button/yt-icon")
        # button.click()
        # button = driver.find_element_by_xpath("//a/div/ytd-channel-name/div/div/yt-formatted-string")
        # button.click()
        # text = driver.find_element_by_xpath('//*[@id="subscribers"]')
        text = driver.find_element(by=By.XPATH, value='//*[@id="subscribers"]')
        if text==None:
            subscribe_list.append([channel, ''])
        else:
            subscribe_list.append([channel, text.text])


        # 寫入一列資料
        writer.writerow([channel, text.text])
driver.close() # 關閉瀏覽器視窗

    # 建立 CSV 檔寫入器

    # for item in subscribe_list:
    #     writer.writerow(item)