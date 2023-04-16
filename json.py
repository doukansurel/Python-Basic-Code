import json

person_string = '{"name" : "Savaş" , "languages":["Python","Java"] }'

#JSON stirng to Dict

#result = json.loads(person_string)


#print(type(result))
#print(result)

#with open("jsonString",encoding="utf-8") as f : 
#    data = json.load(f)
#    print(data)

person_dict = {

    "name": "Ali",
   "languages":"[Python,Java]"
}

#Dict to String 
#result = json.dumps(person_dict)
#print(type(person_dict))

with open("jsonString","w") as file : 
    json.dump(person_dict,file)




