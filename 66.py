# encoding=utf-8

import jieba.posseg as pseg
import jieba
import sys
import asyncio
import telepot
import telepot.async

jieba.initialize()
bot = telepot.async.Bot('217297401:AAHhhGRycynO7MqAc4WcKkCnoc3yFNNO-CA')
loop = asyncio.get_event_loop()
lifecount = 1

def constructmsg(msgtext, lifecount):
    if msgtext == "/+1se":
        print("Lifecount:" + str(lifecount))
        lifecount += 1
        return "续费成功！感谢为 Success 贡献 1 成功值！现在，Success 已经为 LGU 创造 " + str(lifecount * 66) + " 家创业公司！"
    else:
        words = pseg.cut(msgtext)
        reply = ""
        for word, flag in words:
            if flag == 'ns' or flag == 'n' or flag == 'nr' or word == '人' or word == '成功' or word == 'Success':
                reply = reply + '66' + word
            elif word != '/':
                reply = reply + word
                print(word + flag)
        if msgtext[0] != "哇":
            reply = '哇' + reply
        return reply

async def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print (content_type, chat_type, chat_id)
    if content_type == 'text':
        print(msg['text'])
        reply = constructmsg(msg['text'], lifecount)
        await bot.sendMessage(chat_id, reply)
    else:
        reply = "蛤？"
        await bot.sendMessage(chat_id, reply)

loop.create_task(bot.message_loop(handle))
print('Listening ...')
loop.run_forever()
