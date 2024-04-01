#    1. author
#    2. cmt id
#    3. root repo Name
#    4. feature file
#    5. vector of content


from github import Github
from flask import request

from github import Auth

from mongo import MongoConfig
from main import Main
import numpy as np
from sentence_transformers import SentenceTransformer

class ProcessGitHub:

    

    def __init__(self, git = Github(user_agent="aravindh2000",auth=Auth.Token("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")),request=request) -> None:
        self.file_path = []
        self.g = git
        self.request = request
        self.mongo_db = MongoConfig()
        self.encoder = SentenceTransformer("paraphrase-mpnet-base-v2")
        self.num_ins = np.load('op.npy')
        self.np_array = np.array(self.num_ins)
   
    

    def gatherPath(self,url:str):
     split_data = url.split("/")
     final_string = ""
     if split_data.__contains__("Scenarios"):
        index = split_data.index("Scenarios")
        for i in range(index+1,split_data.__len__()):
            final_string+=(split_data[i]+" ")

        self.file_path.append([final_string.strip()])   
    
    
    
    
    def process_repo(self):
        for repo in self.g.get_user().get_repos():
            if repo.name == "Inventory":
                print(repo.name)
                contents = repo.get_contents("")
                while contents:
                 file_content = contents.pop(0)
                 if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path))
                 else:
                    
                    if file_content._html_url.value.__contains__(".feature"):
                     self.gatherPath(str(file_content._html_url.value))


        self.g.close()



    def update_db_with_recent_data(self):
       

       repo_name = self.request.json['repository']['html_url']
       for cmt in self.request.json['commits']:
          changes = cmt['added']

          author =  cmt['author']['username']
          for ind_changes in changes:
             val = str(ind_changes)
             if val.__contains__(".feature"):
                arr = val.split("/")
                file_name = arr[len(arr)-1]
                print(file_name)
                self.mongo_db.collection.insert_one({"author":str(author),"repo_name":str(repo_name),"file_name":str(file_name)})
                self.update_numpy(file_name)
          np.save('op.npy',self.num_ins)      
                
                               
    def update_numpy(self,file_name:str):
        
        row_count = len(self.np_array)
        self.num_ins.resize(row_count+1,768)
        self.num_ins[row_count] = self.encoder.encode(file_name)   
           

# num_ins = np.load('op.npy')
# np_array = np.array(num_ins)
# print(len(np_array))
# num_ins.resize(len(np_array)+1,768)
# print(len(np_array))
# num_ins[len(np_array)] = SentenceTransformer("paraphrase-mpnet-base-v2").encode("Investment banking.feature")
# np.save('op.npy',num_ins)
# print(obj.file_path)

