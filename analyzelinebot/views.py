# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
 
# 取得settings.py中的LINE Bot憑證來進行Messaging API的驗證
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# 歡迎頁面
def index(request):
    return HttpResponse("Welcome to LINE Bot!")

# 健康檢查點
def health_check(request):
    return HttpResponse("OK")

# 處理LINE消息的函数
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  # 如果有消息事件
                handle_message(event)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()

# 處裡不同類型的消息
def handle_message(event):
    text = event.message.text
    
    
    if text.lower() == 'help':
        reply_text = "这是一个LINE机器人。您可以发送消息，我会回复相同的内容。"
    elif text.lower() == 'about':
        reply_text = "这是一个使用Django开发的LINE Bot。"
    else:
        # 默認回復相同的消息
        reply_text = text
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

# 定義一個可以測試的視窗
def test(request):
    return render(request, 'bot_test.html')