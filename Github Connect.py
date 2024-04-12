import streamlit as st
import os
import time
from mongo import MongoConfig
st.set_page_config(page_title="Test Basic Timelines", layout="wide")
st.title("GITHUB CONNECT")
fetch = st.button("Get Latest Feature Entries") 

items = []
db = MongoConfig()
lst = db.collection.find({},{"author":1,"repo_name":1,"file_name":1,"time_stamp":1})
for item in lst:
    items.append([item["file_name"],item["repo_name"],item["time_stamp"]])
    

if fetch:
    if os.path.exists("data"):
            with st.spinner("latest committ lookup..."):
                 time.sleep(8)
            fs = open('data','rb')
            import pickle
            dbs = pickle.load(fs)
            fs.close()
            for k in dbs:
             
             st.toast(dbs[k].file)
             time.sleep(2)
    else:
        st.info('No new feature file committed recently ....', icon="ℹ️")
        #st.write("No new feature file committed recently....")         
if os.path.exists("data"):
         
  os.remove("data") 


git_url = st.text_input(label="Enter Github Url")
automation_repo = st.button("Get Automation Repository") 

if automation_repo:
 with st.spinner("Fetching repo details please wait...."):
    time.sleep(5)

option = st.selectbox(
   'Automation Repository List',
    ('Select','Repo-1', 'Repo-2', 'Repo-3'))

user_filter = st.text_input(label="USER-ID")

if st.toggle('Activate filter'):
    repo_name = st.checkbox("Repository")
import pandas as  pa 
if st.button(label="search"):
    content =  pa.DataFrame(items,columns=['File Name',"Git","Time Updated"]) 
    st.write(content)


from streamlit_timeline import timeline

ct = {
   
   "repo_name":"https://github.com/aravindh2000/Inventory"
   
}


items = [
    {"id": 1, "content": "2022-10-20", "start": "2022-10-20","events": [
        {
          
           
            "start_date": {
                "year":2024,
                "month":4,
                "day":3, 
                "hour": 9,
                "minute": 6,
                "second": 37,
                "microsecond":  880610
            },
            "text": {
                "headline": "creditMapping.feature",
                "text": ct["repo_name"]+"</h4>"
            }
        },
        {
          
           
            "start_date": {
                "year":2024,
                "month":4,
                "day":2, 
                "hour": 9,
                "minute": 6,
                "second": 37,
                "microsecond":  880610
            },
            "text": {
                "headline": "RegO.feature",
                "text": ct["repo_name"]+"</h4>"
            }
        },{
          
           
            "start_date": {
                "year":2024,
                "month":4,
                "day":4, 
                "hour": 9,
                "minute": 6,
                "second": 38,
                "microsecond":  880610
            },
            "text": {
                "headline": "lightRiskEngineResultsUI.feature",
                "text": ct["repo_name"]+"</h4>"
            }
        },
         {
          
           
            "start_date": {
                "year":2024,
                "month":1,
                "day":3, 
                "hour": 9,
                "minute": 6,
                "second": 37,
                "microsecond":  880610
            },
            "text": {
                "headline": "NonARD.feature",
                "text": ct["repo_name"]+"</h4>"
            }
        },{
        "start_date": {
                "year":2024,
                "month":3,
                "day":3, 
                "hour": 9,
                "minute": 6,
                "second": 37,
                "microsecond":  880610
            },
            "text": {
                "headline": "SubmittedForReview_AR.feature",
                "text": ct["repo_name"]+"</h4>"
            }
        }
        
    ]}
    
]

# with open(f'/app/timeline.json', "r") as f:
#     data = f.read()
timeline(items[0], height=600)       
