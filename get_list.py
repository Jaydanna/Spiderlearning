from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

url = 'http://music.163.com/#/discover/'\
      'playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

chrome_options = Options()
chrome_options.add_argument("--headless")

# base_url = "http://www.baidu.com/"
#对应的chromedriver的放置目录
driver = webdriver.Chrome(executable_path=(r'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'), chrome_options=chrome_options)

csv_file = open('playlist.csv','w',newline='')
writer = csv.writer(csv_file)
writer.writerow(['Title','Num','link'])

while url != 'javascript:void(0)':
    # 用webdriver加载页面
    driver.get(url)
    # 切换到内容的iframe
    driver.switch_to.frame("contentFrame")
    # 定位歌单标签
    data = driver.find_element_by_id("m-pl-container").\
        find_element_by_tag_name("li")
    print(type(data))
    # 解析一页中的所有歌单
    for i in range(len(data)):
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split("万")[0]) > 500:
            msk = data[i].find_element_by_css_selector("a.msk")
            writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
    url = driver.find_element_by_css_selector("a.zbtn.znxt").\
        get_attribute('href')
csv_file.close()
