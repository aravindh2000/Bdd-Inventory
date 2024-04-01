# import nltk


# nltk.download('stopwords')

import pandas as pd
# import pdb
from sentence_transformers import SentenceTransformer
from nltk.corpus import stopwords
# from ProcessFeature import ProcessGitHub
# english_stopwords = set(stopwords.words('english'))


# # sentences = []

# # file = open("Feature.txt","r")

# # key = ['scenario:','given','when','then']
# # s2 = " "
# # for line in file.readlines():
# #     if line == "\n":
# #        continue
# #     for words in line.replace('\n','').split(" "):
# #         lower_case = words.lower()
# #         if lower_case == '':
# #            continue
# #         if lower_case not in key and lower_case not in english_stopwords:
# #             s1="".join(c for c in lower_case if c.isalpha())
# #             s2+=str(s1+" ")


# #         else:
# #             continue
# #     if s2 != " ":

# #      sentences.append([s2.strip()])
# #     s2 = " "

# # print(sentences)

# from flask import request
# from github import Github


# from github import Auth
# file_path = []
# def gatherPath(url:str):
#       split_data = url.split("/")
#       final_string = ""
#       if split_data.__contains__("Scenarios"):
#         index = split_data.index("Scenarios")
#         for i in range(index+1,split_data.__len__()):
#             final_string+=(split_data[i]+" ")

#         file_path.append([final_string.strip()])  
# g = Github(user_agent="aravindh2000",auth=Auth.Token("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"))
# for repo in g.get_user().get_repos():
#             if repo.name == "Inventory":
#                 print(repo.name)
#                 contents = repo.get_contents("")
#                 while contents:
#                  file_content = contents.pop(0)
#                  if file_content.type == "dir":
#                     contents.extend(repo.get_contents(file_content.path))
#                  else:
                    
#                     if file_content._html_url.value.__contains__(".feature"):
#                       gatherPath(str(file_content._html_url.value))

                  
# df = pd.DataFrame(file_path,columns=["data"])
# df.head()

# data = df['data']
# print(data)
encoder = SentenceTransformer("paraphrase-mpnet-base-v2")
# embd = encoder.encode(data)

# import numpy as np
from mongo import MongoConfig
# np.save("op.npy",embd)
# db = MongoConfig()
# lst = db.collection.find({})
# lst = []
# for c in lst:
#     lst.append([c['file_name']])
# df = pd.DataFrame([lst],columns=["data"])

class Main:

    def __init__(self,key,count):
       
        self.count=count
        self.key=key
        self.db = MongoConfig()
        self.lst = self.db.collection.find({},{"file_name":1})
        self.final_lst = []
        for ind in self.lst:
            self.final_lst.append([ind['file_name']])
    

    
        

    def run(self):
        
        import numpy as np
        dts = np.load("op.npy")

        df = pd.DataFrame(self.final_lst,columns=["data"])

        data = df['data']
        vector_dimension = dts.shape[1]

        import faiss

        index = faiss.IndexFlatL2(vector_dimension)   # build the index
        print(index.is_trained)
        faiss.normalize_L2(dts)
        index.add(encoder.encode(data))

        

             
        print(index.ntotal)

        


        
        search_text = self.key
        search_vector = encoder.encode(search_text)
        print(search_vector)
        _vector = np.array([search_vector])
        faiss.normalize_L2(_vector)

        # k = 4
        distances, ann = index.search(_vector, k=self.count)

        results = pd.DataFrame({'vector distances': distances[0], 'match score': ann[0]})
        df = pd.DataFrame(self.final_lst,columns=["data"])
        merge = pd.merge(results,df,left_on='match score',right_index=True)

        merge.head()
        # ['data'].values

        print(merge.head())  
        return merge  
