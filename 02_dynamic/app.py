from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route("/") 
def hello(): 
  return "Hello Page!"

@app.route('/profile/<username>') 
def get_profile(username): 
  return 'profile : ' + username 

if __name__ == "__main__": 
  with app.test_request_context(): 
    print (url_for('get_profile', username='flask')) 
    app.run()