from selenium import webdriver
import csv

channels = []
with open(r'C:\Users\GOOD\Desktop\碩班\110-1\IM\final project\code\src\Youtuber名單 - YT_final_list.csv', "r", encoding="utf-8 sig") as f:
    rows = f.read().lower().split('\n')
    for row in rows:
        if row == '' or '頻道(官方帳號)' in row:
            continue
        else:
            words = row.split(',')
            if '"' in words[0]:
                channels.append('Stand up, Brian! 博恩站起來！')
            else:
                channels.append(words[0])
    f.close()
print(channels)


# 開啟瀏覽器視窗(Chrome)
# 方法二：或是直接指定exe檔案路徑
driver = webdriver.Chrome(r'C:\Users\GOOD\Desktop\chromedriver.exe')

start_channel=''
start = True if start_channel == '' else False
csv_write_type = 'w' if start_channel == '' else 'a'

with open('../output/subscribe_list.csv', csv_write_type, newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    if csv_write_type == 'w':
        writer.writerow(['title', 'subscriberCount'])
    for channel in channels:
        if channel == start_channel:
            start = True
        if not start:
            continue

        driver.get("https://www.youtube.com/results?search_query="+channel) # 更改網址以前往不同網頁
        try:
            text = driver.find_element_by_xpath('//*[@id="subscribers"]')
            writer.writerow([channel, text.text])
            # count_txt = text.text.replace(',','').replace(' ','').replace('位訂閱者','')
            # count = float(count_txt)*10000 if '萬' in count_txt else float(count_txt)
            # writer.writerow([channel, count])
        except ValueError:
            writer.writerow([channel, ''])
driver.close() # 關閉瀏覽器視窗
