#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def test():
    message = TemplateSendMessage(
        alt_text='解題小幫手',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/5rnnEKZ.jpg",
                    action=URITemplateAction(
                        label="進位紀錄",
                        uri="https://i.imgur.com/5rnnEKZ.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/9JTIUbi.jpg",
                    action=URITemplateAction(
                        label="進位加法",
                        uri="https://i.imgur.com/9JTIUbi.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/qlGNUB4.jpg",
                    action=URITemplateAction(
                        label="整數倍規律",
                        uri="https://i.imgur.com/qlGNUB4.jpg"
                    )
                ),
            ]
        )
    )
    return message