import pymongo
from Academic_Calender import get_url
from Alert import find_fail,find_fee
client = pymongo.MongoClient("mongodb+srv://Hit:abc@cluster.qcrpjef.mongodb.net/test")
db = client['PID616']
student_collection = db['student_data']
user_collection=db['user_data']

# user_collection.insert_one({"usrename":"hit"})
def student_insert(data):
    student_collection.insert_one(data);

def Search(data):

    return "hi"
def user_insert(data):
    # print(data)
    data1 = data['queryResult']['action']
    print(data1)
    ans=""
    if(data1=="Studentcorner.Studentcorner-custom.Exam-custom.Result-custom.Result-Sem-custom.Result-Sem-ID-custom"):
        ID = data["queryResult"]["parameters"]["ID"]
        Pas = data["queryResult"]["parameters"]["password"]
        ID=str(int(ID))
        print(ID)
        print(Pas)
        sem=data["queryResult"]["outputContexts"][0]['parameters']["sem.original"]
        # print(sem)
        try:
            student=student_collection.find_one({"Enrolment id":ID}, {"result": 1,"password":1,"_id": 0})
            rpas=student["password"]
            if(rpas!=Pas):
                ans += "your password was incorrect"
                return ans
            print(student)
        except:
            ans = '' + "Dada base System ma nathi"
            return ans
        if(student==None):
            ans = '' + "Dada base System ma nathi"
            return ans
        string='sem'+sem
        # print(string)
        # print(student)
        # print(student['result'])
        print(student)
        student=student['result'][string]
        # print(student)
        ans=""
        for key in student:
            ans+=key+" : "
            if type(student[key]) is dict:
                ans+='\n'
                for k in student[key]:
                    ans+='\t'+k+" :" +student[key][k]+"\n"
            else:
                ans+=student[key]+"\n"
        # print(ans)
        return ans
    elif(data1=="Studentcorner.Studentcorner-custom-2.Academics-custom.Attendence-custom.ID-custom"):
        ID = data["queryResult"]["parameters"]["ID"]
        pas = data["queryResult"]["parameters"]["password"]
        ID=str(int(ID))
        print(ID)
        print(pas)
        try:
            student = student_collection.find_one({"Enrolment id": ID}, {"attendence": 1,"password":1,"_id": 0})
            rpas=student["password"]
            if(rpas!=pas):
                ans += "your password was incorrect"
                return ans
        except:
            ans = '' + "Dada base System ma nathi"
            return ans
        if (student == None):
            ans = '' + "Dada base System ma nathi"
            return ans
        # print(student)

        student = student['attendence']["sem1"]
        # print(student)
        for key in student:
            ans += key + " : "
            if type(student[key]) is dict:
                ans += '\n'
                for k in student[key]:
                    ans += '\t' + k + " :" + student[key][k] + "\n"
            else:
                ans += student[key] + "\n"
        # print(ans)
        return ans
    elif(data1=="Studentcorner.Studentcorner-custom-3.Fees-custom.Fees-Sem-custom.Fees-Sem-ID-custom"):
        ID = data["queryResult"]["parameters"]["ID"]
        pas = data["queryResult"]["parameters"]["password"]
        ID=str(int(ID))
        # print(ID)
        # print(pas)
        sem=data["queryResult"]["outputContexts"][0]['parameters']["sem"]
        # print(sem)
        student={}
        try:
            student = student_collection.find_one({"Enrolment id": ID}, {"fees": 1,"password":1, "_id": 0})
            rpass=student["password"]
            print(rpass)
            print(student)
            if (student == None):
                ans = '' + "Data not found"
                return ans
        except:
            ans = '' + "Dada base System ma nathi"
            return ans

        if(rpass==pas):
            # print(student["fees"])
            student=student["fees"][sem]
            print(student)
            for key in student:
                ans+=key + ":"+student[key]+"\n"
            return ans
        else:
            ans+="your password was incorrect"
            return ans
    elif(data1=="Studentcorner.Studentcorner-custom-2.Academics-custom"):
        ans=get_url()
        print("ans= \n"+ans)
        if (ans == None):
            ans = '' + "Data not found"
            return ans
        return ans

    elif(data1=="Register.Register-custom.registergtuid-custom"):
        # print(data)
        ID=data["queryResult"]["parameters"]["ID"]
        pas=data["queryResult"]["parameters"]["Password"]
        ID = str(int(ID))
        # print(ID)

        chatID=data["originalDetectIntentRequest"]["payload"]["data"]["chat"]["id"]
        ID=str(int(ID))
        user={
            "GTU_ID":ID,
            "ChatID":chatID,
            "Password":pas
        }
        print(user)
        u=user_collection.find_one({"GTU_ID":ID})
        if(u==None):
            user_collection.insert_one(user)
            ans += "You Are Registered in Database"
            return ans
        else:
            ans += "You can not register Twice"
            return ans
        # print(user)
        # print(ans)

    # print()
    # print(data1)
    elif(data1=="Atkt"):

        x=data['queryResult']["parameters"]["text"]
        # y =data['from']['ID']
        print(x)
        find_fail(x)
        return "hii"
        # find_fail(x)
    elif(data1=="Pending.fee"):
        # print("feeeeeee")
        message=data["queryResult"]["parameters"]["text"]
        find_fee(message)
    else:
        ans=''+"Dada base System ma nathi"
        return ans


# print(
# user_insert(
#
# {'responseId': 'da3328ab-fd64-4c79-baa2-a3ee0a5c47cf-d3dc5474', 'queryResult': {'queryText': '/kt dhandhama dhyan aapo', 'action': 'Atkt', 'parameters': {'text': 'dhandhama dhyan aapo'}, 'allRequiredParamsPresent': True, 'fulfillmentText': 'hello', 'fulfillmentMessages': [{'text': {'text': ['hello']}}], 'outputContexts': [{'name': 'projects/gtu-kjqk/agent/sessions/98eab328-d16a-3c53-92f1-973fdda71654/contexts/__system_counters__', 'parameters': {'no-input': 0.0, 'no-match': 0.0, 'text': 'dhandhama dhyan aapo', 'text.original': 'dhandhama dhyan aapo'}}], 'intent': {'name': 'projects/gtu-kjqk/agent/intents/d8f889e3-bcb9-4c24-9453-448bde176a63', 'displayName': 'ATKT'}, 'intentDetectionConfidence': 0.71786344, 'languageCode': 'en'}, 'originalDetectIntentRequest': {'source': 'telegram', 'payload': {'data': {'entities': [{'type': 'bot_command', 'length': 3.0}], 'text': '/kt dhandhama dhyan aapo', 'message_id': '4721', 'from': {'username': 'HitKoladiya', 'last_name': 'Koladiya', 'language_code': 'en', 'first_name': 'Hit', 'id': '1106613031'}, 'date': '1665212568', 'chat': {'type': 'private', 'id': '1106613031'}}}}, 'session': 'projects/gtu-kjqk/agent/sessions/98eab328-d16a-3c53-92f1-973fdda71654'}
# )
# )
# user_insert(data)
# user_insert(data)#
# ({"instituteName": data["instituteName"]}, {"_id": 0})
