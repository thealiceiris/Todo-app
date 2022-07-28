from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)
app.debug = True

class Item:
    id= ""
    title = ""
    desc = ""
    username = ""
    password = ""
    email = ""
    confirmed = ""
    user_type_id= ""

    def __init__(self, id, title, desc, username, password, email, confirmed, user_type_id):
        self.id = id
        self.title = title
        self.desc = desc
        self.username = username
        self.password = password
        self.email = email
        self.confirmed = confirmed
        self.user_type_id = user_type_id      

    def toJson(self):
        in_json = {"id":self.id, "title" : self.title, "desc": self.desc, "username":self.username,
        "password":self.password, "email": self.email,"confirmed": self.confirmed, "user_type_id":self.user_type_id}
        return in_json

    def toJson2(self):
        return self.__dict__

toDoList = []

item1 = Item(id="1", title="scrub",desc= "scrub 3 bathrooms by 3pm on sunday", username= "aliceiris", password= "crazymeangirls", 
email="aliceiris@gmail.com", confirmed="yes", user_type_id= "students")
item2 = Item(id="2", title="homework",desc= "do my homework on computer algorthims", username= "aliceiris", password= "crazymeangirls", 
email="aliceiris@gmail.com", confirmed="yes", user_type_id= "students")

toDoList.append(item1.toJson())
toDoList.append(item2.toJson2())
print(toDoList)

@app.route("/todo/list")
def getAllToDos():
    return jsonify(toDoList)                                                                                                                                                                                                                                                   

@app.route("/todo", methods=["POST"])
def createNewToDoItem():
    item =Item(**request.get_json())
    toDoList.append(item.toJson())
    return Response('{"message": "success"}', status =201, mimetype= 'application/json')

@app.route("/todo/<id>")
def findToDoItemById(id):
    itemToReturn = None
    for item in toDoList:
        if item("id") == id:
            itemToReturn = item
        else:
            continue
    if itemToReturn == None:
        return Response('{"message": "item not found"}', status =404, mimetype= 'application/json')
    else:
        Response = jsonify(itemToReturn)
        Response.status_code =200
    return Response
 
@app.route("/todo", methods=["PUT"])
def updateExistingToDoItem():
     item=Item(**request.get_json())
     isExist = False
     for i in toDoList:
        if i("id") == item.id:
           i("title")== item.title
           i("desc") == item.desc
           i("username") == item.desc
           i("password")== item.password
           i("email") == item.email
           i("confirmed") == item.confirmed
           i("user_type_id") == item.user_type_id
           isExist = True
           break 
     if isExist:
        response = jsonify('{"message": "item updated successfully"}')    
        response.status_code = 201 
        return response
     else:
        response = jsonify('{"message": "item does not exist"}')    
        response.status_code = 404
        return response

@app.route("/todo", methods=["DELETE"])
def deleteToDoItembyId(id):
    itemToDelete= None
    for item in toDoList:
        if item ("id")== id:
            itemToDelete = item
        else:
            continue
    if itemToDelete == None:
         response = jsonify('{"message": "item does not exist"}')    
         response.status_code = 201
         return response
    else:
        response = jsonify('{"message": "item does not removed successfully"}')    
        response.status_code = 200
        return response

if __name__ == "__main__":
   app.run(port=8181) 