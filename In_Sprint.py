
# PageOne contents 
#  ATATT3xFfGF0gHt7JhwD0AjFi80mzI2dd8yK_YMYSU81agZWDXwSbtafEPmHwMRLX76PWdSsN3xA2YWPPGx0dB7oXrpE1zxha5eOka0RAomJYoR5xRNxCjrbwoI-dMI62CgB2i9Qb-JvpP2GNVqkT7mqFirJTKFUPbs2gQxxJU4GXmnIeYNMeO0=9E34D3E2 
import streamlit as stm 

  
stm.title("In-Sprint Automation Data")

from jira import JIRA 
from streamlit_card import card
import pandas as pa
from mongo import MongoConfig
import requests
from main import Main
class JiraConfig:

    def __init__(self):
        
        self.jiraOptions = {'server': "https://aravindhsiva9.atlassian.net"} 
        self.jira = JIRA(options=self.jiraOptions, basic_auth=( 
    "aravindhsiva9@gmail.com", "ATATT3xFfGF0gHt7JhwD0AjFi80mzI2dd8yK_YMYSU81agZWDXwSbtafEPmHwMRLX76PWdSsN3xA2YWPPGx0dB7oXrpE1zxha5eOka0RAomJYoR5xRNxCjrbwoI-dMI62CgB2i9Qb-JvpP2GNVqkT7mqFirJTKFUPbs2gQxxJU4GXmnIeYNMeO0=9E34D3E2")) 

  
stm.session_state['data_frame'] = pa.DataFrame()

if "my_input" not in stm.session_state:
    stm.session_state["my_input"] = []
    stm.session_state['card'] = False
    stm.session_state['key'] = ''
    stm.session_state["up"] = False
    stm.session_state['fetch'] = False
    
    
    
    

name = stm.text_input('JIRA KEY')

clicked = stm.button("Fetch JIRA")

if clicked:
    obj = JiraConfig()
    singleIssue = obj.jira.issue(name) 
    header_val = singleIssue.fields.summary
    des_val = singleIssue.fields.description
    stm.session_state['key'] = singleIssue.fields.description
    key = singleIssue.key
    hasClicked = card(
  title="JIRA : "+key,
  text=header_val+" : "+des_val,
  
)  

    stm.session_state['card'] = True
fetch = stm.button("Get Feature File") 
stm.session_state['fetch'] = fetch  


        

# if stm.session_state['fetch'] and stm.session_state["up"] == True:
#     uploaded_file = stm.file_uploader("Upload file to ISSUE")       
#     if uploaded_file:
#             df = pa.read_csv(uploaded_file)
#             stm.write(df.head()) 
uploaded_file = stm.file_uploader("Upload file to ISSUE") 
import time


       
if stm.session_state['fetch']:
        print(stm.session_state['card'],"is clicked")
        
        obj = Main(stm.session_state['key'],3)
        merge = obj.run()
        stm.session_state["my_input"] = merge
        mg_config = MongoConfig()
        filter_list = stm.session_state["my_input"]['data'].values
        dt = []
        df  = pa
        print(filter_list)
        for ind in filter_list:
      
          flt_data = mg_config.collection.find({},{"file_name":ind,"author":1,"repo_name":1,'time_stamp':1})
          print(flt_data)
          dt.append([flt_data[0]['file_name'],flt_data[0]['author'],flt_data[0]['repo_name'],flt_data[0]['time_stamp']])
          print(dt)
          df = pa.DataFrame(dt,columns=['File Name','Author',"Git","Time Updated"])
        if df is not None:
          with stm.spinner('loading feature files'):
               time.sleep(5)
        
              
          stm.session_state['data_frame'] = df
        stm.session_state["up"] = True
        
stm.write(stm.session_state['data_frame'])

import os  
   
if uploaded_file:
    
    url = 'https://aravindhsiva9.atlassian.net/rest/api/3/issue/KAN-1/attachments'
    data_frame = pa.read_csv(uploaded_file)
    data_frame.to_csv("related_feature_files_tmp.csv",sep='\t', encoding='utf-8')
    data_frame = None
    # data_frame.to_csv("related_feature_files_tmp.csv",sep='\t', encoding='utf-8')
    f = open("related_feature_files_tmp.csv","rb")
    file = {
        "file":("related_feature_files_tmp.csv",f)
    }
    

    headers ={
        'X-Atlassian-Token' : 'no-check'
    } 
    response = requests.post(url,headers=headers,files=file,auth=("aravindhsiva9@gmail.com", "ATATT3xFfGF0gHt7JhwD0AjFi80mzI2dd8yK_YMYSU81agZWDXwSbtafEPmHwMRLX76PWdSsN3xA2YWPPGx0dB7oXrpE1zxha5eOka0RAomJYoR5xRNxCjrbwoI-dMI62CgB2i9Qb-JvpP2GNVqkT7mqFirJTKFUPbs2gQxxJU4GXmnIeYNMeO0=9E34D3E2"))                  
    f.close()
    file_path = 'related_feature_files_tmp.csv'
    os.remove(file_path)
    with stm.spinner('uploading file to JIRA...'):
        time.sleep(5)
        stm.success('Done!')

# fs = open('data','rb')
# import pickle
# from ProcessFeature import Bundle as bd
# dbs = pickle.load(fs)

# for k in dbs:
#     time.sleep(2)
#     stm.toast(dbs[k].file)
# fs.close()
# os.remove("data")    
    


# import socket

  
# host = '192.168.1.3'
# port = 8502

# s = socket.socket(socket.AF_INET,
#                   socket.SOCK_STREAM)
# s.connect((host, port))

# msg = s.recv(1024)

# while msg:
#     print('Received:' + msg.decode())
#     stm.toast(msg.decode()+" has been added")
#     time.sleep(.5)
#     msg = s.recv(1024)



    



        


    
    
