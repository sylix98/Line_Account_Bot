# LINE 記帳機器人

本專案為使用 Python + Flask + SQLite + LINE Messaging API 所打造的 LINE 記帳機器人，支援多用戶記帳與查詢功能，部署於 Render 雲端平台，並透過 UptimeRobot 保持常駐運作。\
演示影片：

## 功能特色

- 支援 LINE 個人帳號互動
- 可輸入簡易格式記帳（例如：「午餐 100」）
- 輸入「查今天」顯示當天記帳紀錄
- 若多人使用時會自動區分帳號，避免資料混淆
- 雲端部署於 [Render](https://render.com/)
- 搭配 [UptimeRobot](https://uptimerobot.com/) 定時喚醒，避免休眠

---

## 結構介紹

| 檔案 | 說明 |
|------|------|
| db.py | 資料庫的初始化與操作 |
| line_account_bot.py | Flask 主應用程式，用來傳送與處理 LINE Webhook |
| requirements.txt | 需求套件 |
| Procfile | 在 Render 中用來啟動程式的指令 |

---

## 使用技術

| 技術 | 說明 |
|------|------|
| Python | 核心開發語言 |
| Flask | Web 框架，用來接收 LINE Webhook |
| SQLite | 輕量化的資料庫，記錄使用者的帳務資料 |
| line-bot-sdk | LINE 官方提供的 Python SDK |
| Render | 雲端主機，24小時部署後端伺服器 |
| UptimeRobot | 定時喚醒服務，避免 Render 免費方案進入睡眠狀態 |

---

##  使用方法

### 1. 安裝依賴套件
```bash
git clone https://github.com/你的帳號/Line_Account_bot.git
pip install -r requirements.txt
```

### 2. 啟動 Flask 開發伺服器
```bash
python line_account_bot.py //進行本機測試
```

### 3. 部署到 Render 
專案中包含 requirements.txt 和 Procfile。\
只需將此專案推送至 GitHub 並連接至 Render 即可自動部署。

### 4. 設置UptimeRobot(非必要)
由於本專案使用 Render 免費方案，因此閒置15分鐘後將進入休眠狀態，容易造成顯著延遲。\
將 Render 網址(Render部署成功後所提供) 連接至UptimeRobot中，每10分鐘進行一次 ping，保持伺服器運作。

### 5. 加入Line帳號進行使用
Line記帳小助手 @311wyyeh\
在對話框中輸入「午餐 100」即可記帳。\
在對話框中輸入「查今天」可檢視紀錄。

---

## 注意事項
- 本專案僅用於個人練習用途，尚未進行帳號驗證與進階安全控制！
- 目前預計可擴充功能如「月份統計」、「雲端資料庫」、「LINE rich menu」等。
---
