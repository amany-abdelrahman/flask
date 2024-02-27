from flask import Flask, request

app=Flask(__name__)
users=[{"id":1,"name":"amany"},{"id":2,"name":"amira"},{"id":3,"name":"anas"}]

@app.route('/') 
def index():
    # print(name)
    return "<h1 style= 'text-align: center'>Helloooooooooo</h1>"
# app.add_url_rule('/','index',index)


@app.route('/users')
def get_users():
    # print(dir(request))
    print(request.method)
    print(request.args)
    return "user"


if __name__ == '__main__':
    app.run(debug=True)