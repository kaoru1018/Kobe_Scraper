from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.google.com/maps/search/神戸牛")
time.sleep(5) # ここを少し短くしました

# お店全体の枠を取得する
# Googleマップのリスト項目は "m6QErb" というクラスでまとまっています
places = driver.find_elements(By.CLASS_NAME, "m6QErb")

data = []
for place in places:
    try:
        # 名前と評価を個別に探す
        name = place.find_element(By.CLASS_NAME, "qBF1Pd").text
        rating = place.find_element(By.CLASS_NAME, "MW4etd").text
        data.append({"店名": name, "評価": rating})
    except:
        continue # うまく取れなかった項目は飛ばす

# CSVに保存
df = pd.DataFrame(data)
df.to_csv("kobe_beef_with_rating.csv", index=False, encoding="utf-8-sig")

print("名前と評価の保存が完了しました！")