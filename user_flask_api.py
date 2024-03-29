from flask import Flask, request

app = Flask(__name__)
users = [ {"id": 1, "username": "yaron", "password": "123", "salary": 8000, "address": "hanarkis  St", "active": True},
 {"id": 2, "username": "josh", "password": "456", "salary": 60000, "address": "456 Oak St", "active": False}
]


def add_key(k_a,dict_a):
    new_dict = {}
    for k, v in dict_a.items():
        new_dict[k] = v
    new_dict[k_a] = True
    return new_dict
def rem_key(k_a,dict_a):
    new_dict = {}
    for k,v in dict_a.items():
        if k != k_a:
            new_dict[k] = v
    return new_dict


def check_empty(dict_user):
    for user in dict_user:
        if user["active"]:
            return True
    return False


# GET -> return all the movies
@app.get('/users')
def get_all_users():
    '''
    this function return all the users
    '''
    if check_empty(users):
        filtered = [rem_key(k_a="active",dict_a=user) for user in users if user["active"]]
        return filtered
    else:
        return "user table empty"


# GET /id -> return one movie
@app.get('/users/<int:id>')
def get_user(id):
    '''
    :param id:  user id
    :return: the user dict
    '''
    for user in users:
        if user['id'] == id and user["active"]:
            return rem_key(k_a="active",dict_a=user)
    return 'data not found', 400  # return message/data , status code


# POST -> add user to the list

@app.post('/users')
def add_user():
    user = request.json  # takes the body and convert the json to dict

    user['id'] = users[-1]['id'] + 1
    users.append(add_key(k_a="active",dict_a=user))
    return "user was added succesfuly"


# put -> change movie
@app.put('/users/<int:id>')
def change_user(id):
    new_user = request.json  # take the new user from the body of the request
    for i in range(len(users)):  # iterate over all the users indexes
        if users[i]['id'] == id and users[i]['active']:  # if the id of the user matches the param id
            users.pop(i)  # remove the old user
            users.insert(i, add_key(k_a="active",dict_a=new_user))  # add new user
            return 'user update done'
    return 'user update failed'


# delete -> remove all the users
@app.delete('/users')
def delete_all_users():
    for i in range(len(users)):
        users[i]["active"] = False
    return "all user were deletted"


# delete /id -> delete one user
@app.delete('/user/<int:id>')
def delete_user(id):
    for i in range(len(users)):
        if users[i]['id'] == id:
            users[i]["active"] = False
            return f"user {id} was deleted"
    return f"user {id} not found"


# aa = 1
app.run()