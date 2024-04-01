from flask import Flask
from flask import request
from flask import json  
from flask_ngrok import run_with_ngrok
from ProcessFeature import ProcessGitHub


app = Flask(__name__)
# run_with_ngrok(app)

@app.route('/')
def root():
  return 'Hello World!'

@app.route('/events', methods=['POST']) 
def hook_root():
  if request.content_type == 'application/json':  
    print(json.dumps(request.json))
    process_changes = ProcessGitHub(request=request)
    process_changes.update_db_with_recent_data()
    return 'hello'

if __name__ == '__main__':
  app.run()

