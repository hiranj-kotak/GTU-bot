from bot_message import send_message
import pymongo
# from Academic_Calender import get_url
client = pymongo.MongoClient("mongodb+srv://Hit:abc@cluster.qcrpjef.mongodb.net/test")
db = client['PID616']
student_collection = db['student_data']
user_collection=db['user_data']
# x=.find({"result":"sem6"})
def find_fail(data):
    x=student_collection.find({})
    # print(x)
    ans=[]
    for i in x:
        # print(type(i))

        test=i["result"]["sem3"]["no of backlogs"]
        if(int(test)>0):
            ans.append(i["Enrolment id"])
        # print(i)
        # print(test)
    print(ans)
    nango=[]
    # nango.append(2068289260)
    for nang in ans:
        print("under")
        x=user_collection.find_one({"GTU_ID":nang},{"ChatID":1,"_id":0})
        print(x)
        if(x!=None):
            print(x)
            nango.append(x["ChatID"])
    print(nango)
    send_message(nango,data)

def find_fee(data):
    x = student_collection.find({})
    fees=[]
    pending_fee=[]
    fee_stat=[]
    for i in x:
        # print(i)
        z=i["fees"]["sem4"]["pending"]
        if(int(z)>0):
           fees.append(i["Enrolment id"])
    # print(fees)
    for id in fees:
        chatid=user_collection.find_one({"GTU_ID":id},{"ChatID":1,"_id":0})
        if(chatid!=None):
            pending_fee.append(chatid["ChatID"])
    # print(pending_fee)
    send_message(pending_fee,data)


# db.inventory.find( { price: { $not: { $gt: 1.99 } } } )