import pymongo
client = pymongo.MongoClient("mongodb+srv://Hit:abc@cluster.qcrpjef.mongodb.net/test")
db = client['PID616']
student_collection = db['student_data']
user_collection=db['user_data']

user_collection.insert_one({"usrename":"hit"})
def student_insert(data):
    student_collection.insert_one(data);

def Search(data):

    return "hi"
def user_insert(data):
    data1=data['queryResult']['action']
    if(data1=="Studentcorner.Studentcorner-custom.Exam-custom.Result-custom.Result-Sem-custom"):
        ID=data["queryResult"]["parameters"]["ID"]
        # print(ID)
        sem=data["queryResult"]["outputContexts"][0]['parameters']["sem.original"]
        # print(sem)
        student=student_collection.find_one({"Enrolment id":"21it068"}, {"result": 1,"_id": 0})
        string='sem'+sem
        # print(string)
        # print(student)
        # print(student['result'])
        student=student['result'][string]
        print(student)
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



# user_insert({'responseId': '7391b890-7dc8-440f-b4d2-0fa4a52338a8-d3dc5474', 'queryResult': {'queryText': '21it068', 'action': 'Studentcorner.Studentcorner-custom.Exam-custom.Result-custom.Result-Sem-custom', 'parameters': {'ID': '21it068'}, 'allRequiredParamsPresent': True, 'fulfillmentMessages': [{'text': {'text': ['']}}], 'outputContexts': [{'name': 'projects/gtu-kjqk/agent/sessions/17daf4b3-a0a2-3f84-ad14-ded2256a7687/contexts/result-followup', 'parameters': {'sem': 1.0, 'sem.original': '1', 'ID': '21it068', 'ID.original': '21it068'}}, {'name': 'projects/gtu-kjqk/agent/sessions/17daf4b3-a0a2-3f84-ad14-ded2256a7687/contexts/result-sem-followup', 'lifespanCount': 1, 'parameters': {'sem': 1.0, 'sem.original': '1', 'ID': '21it068', 'ID.original': '21it068'}}, {'name': 'projects/gtu-kjqk/agent/sessions/17daf4b3-a0a2-3f84-ad14-ded2256a7687/contexts/__system_counters__', 'parameters': {'no-input': 0.0, 'no-match': 0.0, 'ID': '21it068', 'ID.original': '21it068'}}], 'intent': {'name': 'projects/gtu-kjqk/agent/intents/12e5a54e-33d4-4924-bd33-04937a0a6957', 'displayName': 'Result-Sem - ID'}, 'intentDetectionConfidence': 1.0, 'languageCode': 'en'}, 'originalDetectIntentRequest': {'source': 'telegram', 'payload': {'data': {'date': '1665156262', 'chat': {'id': '2084389374', 'type': 'private'}, 'from': {'first_name': 'Kotak Hiranj', 'id': '2084389374', 'username': 'kotakhiranj', 'language_code': 'en'}, 'text': '21it068', 'message_id': '1297'}}}, 'session': 'projects/gtu-kjqk/agent/sessions/17daf4b3-a0a2-3f84-ad14-ded2256a7687'})
# # user_insert(data)
# # ({"instituteName": data["instituteName"]}, {"_id": 0})

# safe_string = urllib.quote_plus('string_of_characters_like_these:$#@=?%^Q^$')