# Kobe_Scraper

## プロジェクト概要
このプロジェクトは、Pythonを使用して神戸牛を取り扱う店舗情報をWebサイトから自動収集（スクレイピング）し、リスト化および評価の整理を行うツールです。

## 主な機能
- Webサイトからの店舗名データの自動抽出
- 抽出データのCSVファイル保存 (`kobe_beef_list.csv`)
- 取得データへの評価付与と統合 (`kobe_beef_with_rating.csv`)

## 使用している技術・ライブラリ
- Python
- Pandas
- BeautifulSoup (Beautiful Soup 4)
- requests

## 実行方法
1. ターミナルで本リポジトリのディレクトリに移動します。
2. 以下のコマンドを実行してスクレイピングと評価データの生成を行います。

```bash
python scrape_kobe_v2_rating.py
