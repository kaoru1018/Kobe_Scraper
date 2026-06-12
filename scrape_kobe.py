from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd  # データを表形式にするためのツール

# ブラウザ設定
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.google.com/maps/search/神戸牛")
time.sleep(10)

# お店リストを抽出
names = driver.find_elements(By.CLASS_NAME, "qBF1Pd")
name_list = [name.text for name in names]

# リストを表（DataFrame）にしてCSVとして保存
df = pd.DataFrame(name_list, columns=["店名"])
df.to_csv("kobe_beef_list.csv", index=False, encoding="utf-8-sig")

print("保存が完了しました！")