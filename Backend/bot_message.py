import requests
tocken = "5760945632:AAGsu3dZp176RmWuL9cOuXsRVai1rNNjTds"



def send_message(chat_ids, text):
    for chat_id in chat_ids:
        base_url = f"https://api.telegram.org/bot{tocken}/sendMessage?chat_id={chat_id}&text={text}"
        print(base_url)
        requests.get(base_url)
        print("message sent")


 #https://api.telegram.org/bot/5760945632:AAGsu3dZp176RmWuL9cOuXsRVai1rNNjTds/getUpdates
# send_message([1106613031,2068289260,1944303878],"you are failed")