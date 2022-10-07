import telepot

def bot_message():
    token = '5760945632:AAGsu3dZp176RmWuL9cOuXsRVai1rNNjTds' # telegram token
    receiver_id = 2084389374 # https://api.telegram.org/bot<TOKEN>/getUpdates


    bot = telepot.Bot(token)

    bot.sendMessage(receiver_id, 'This is a automated test message.') # send a activation message to telegram receiver id

# bot.sendPhoto(receiver_id, photo=open('test_img.png', 'rb')) # send message to telegram