from flask import Flask,request,render_template,redirect

app=Flask(__name__,template_folder="templates") 

users=[]
def get_next_id():
    if len(users)>0:
        return users[-1]['id']+1
    else :
        return 1
    
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users')
def get_users():
    name=request.args.get('name')
    age=request.args.get('age')
    location=request.args.get('location')
    if name != None or age != None or location != None :
        users.append({"id":get_next_id(),"name":name,"age":age,"location":location})
    if users != []:
        return render_template('users.html',users_html=users)
    else :
        return "<h1 style='text-align: center;'> List of users is empty</h1>"

@app.route('/delete/<int:id>')
def delete_user(id):
    if id != None and len(users) !=0 : 
        for i in range(len(users)):
            if users[i]['id']==id:
                del users[i]
                break

    return redirect('/users')

@app.route('/edit/<int:id>')
def edit_user(id):
    edit_name = request.args.get('name')
    edit_age = request.args.get('age')
    edit_location = request.args.get('location')
    for user in users:
        if user['id'] == int(id):
            if edit_name is not None:
                user['name'] = edit_name
            if edit_age is not None:
                user['age'] = edit_age
            if edit_location is not None:
                user['location'] = edit_location
            break
    else:
        return "<h1 style='text-align: center;'>This id not found in the list</h1>"
    return redirect('/users')




# @app.route('/edit/<int:id>') 
# def edit_user(id):
#     edit_name = request.args.get('name')
#     edit_age = request.args.get('age')
#     edit_location = request.args.get('location')
    
#     for user in users:
#         if user['id'] == id:
#             updates = {}
#             if edit_name is not None:
#                 updates['name'] = edit_name
#             if edit_age is not None:
#                 updates['age'] = edit_age
#             if edit_location is not None:
#                 updates['location'] = edit_location
#             user.update(updates)
#             break
    
#     return redirect('/users')




if __name__ == "__main__" :
    app.run(debug=True)