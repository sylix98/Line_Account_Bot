# line_account_bot.py
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from db import init_db, add_record, today_records  # db.py

app = Flask(__name__)

line_bot_api = LineBotApi('VgUc0qEAgQku1rzSsOrZNSeajqINoUhMkPuEKCGLvISs4k8EB3u+2CBrGZh/ZQeMK8dvteFqLpmna9CnbQpmmHDAladu6ltBQVwxd+RKjAZvFEYr54WAYNkSBjptTfCnPozPV9iAj7vYPCFTC6Q8tgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e04673319d083ffb207202fed7e13e3e')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id()
    msg = event.message.text.strip()
    if msg.startswith("查今天"):
        records = today_records(user_id)
        if not records:
            reply = "今天還沒有記帳紀錄。"
        else:
            reply = "\n".join([f"{r[0]}: {r[1]} 元" for r in records])
    else:
        try:
            category, amount = msg.split()
            amount = int(amount)
            add_record(user_id, category, amount)
            reply = f"已記下：{category} {amount} 元"
        except:
            reply = "格式錯誤！請用「午餐 100」記帳，或輸入「查今天」查詢"

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

# 初始化資料庫並啟動伺服器
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=10000)
