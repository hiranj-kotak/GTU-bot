import requests
tocken = "5760945632:AAGsu3dZp176RmWuL9cOuXsRVai1rNNjTds"



def send_message(chat_ids, text):
    for chat_id in chat_ids:
        base_url = f"https://api.telegram.org/bot{tocken}/sendMessage?chat_id={chat_id}&text={text}"
        requests.get(base_url)


 #https://api.telegram.org/bot/5760945632:AAGsu3dZp176RmWuL9cOuXsRVai1rNNjTds/getUpdates