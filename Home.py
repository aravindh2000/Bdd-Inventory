import streamlit as st
from streamlit_option_menu import option_menu
from main import Main
import pandas as pa
from mongo import MongoConfig
#x3TGgsm1TSYD7kzL
#mongodb+srv://aravindhsiva9:x3TGgsm1TSYD7kzL@cluster0.hg9a4yb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

st.set_page_config(
    page_title="BDD Inventory",
)

st.title("Search for features")
if "my_input" not in st.session_state:
    st.session_state["my_input"] = []
    st.session_state["ip"]='INPUT'

my_input = st.text_input("provide your search key")
values = st.slider(
    'Select return count',
    0, 50)

author_detail = st.checkbox("Autor Detail")
repo_name = st.checkbox("Repo")
submit = st.button("Submit")

if submit :
    if my_input != "":
      print("inside submit")
      obj = Main(my_input,values)
      merge = obj.run()
      st.session_state["my_input"] = merge
      st.write(merge)
    else:
       st.write("Please provide search key")  

if author_detail:
   mg_config = MongoConfig()
   filter_list = st.session_state["my_input"]['data'].values
   dt = []
   df = pa
   print(filter_list)
   for ind in filter_list:
      print(ind)
      flt_data = mg_config.collection.find({},{"file_name":ind,"author":1})
      print(flt_data)
      dt.append([flt_data[0]['file_name'],flt_data[0]['author']])
      print(dt)
      df = pa.DataFrame(dt,columns=['File Name','Author'])
      
   
   st.write(df)   

   print(filter_list)


if repo_name:
   mg_config = MongoConfig()
   filter_list = st.session_state["my_input"]['data'].values
   dt = []
   df = pa
   print(filter_list)
   for ind in filter_list:
      print(ind)
      flt_data = mg_config.collection.find({},{"file_name":ind,"author":1,"repo_name":1})
      print(flt_data)
      dt.append([flt_data[0]['file_name'],flt_data[0]['author'],flt_data[0]['repo_name']])
      print(dt)
      df = pa.DataFrame(dt,columns=['File Name','Author',"Git"])
      
   st.session_state["my_input"] = []
   st.write(df)   

   print(filter_list)   

   
   
          



# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)



