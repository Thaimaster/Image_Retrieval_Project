#!/usr/bin/env python
# coding: utf-8

# In[98]:


from pathlib import Path
import numpy as np
from Feature_Extractor import FeatureExtractor
from PIL import Image
import os 
import matplotlib.pyplot as plt


# In[56]:



def absolute_difference(x, query, axis=None):
    return np.sqrt(np.sum((x-query)**2, axis =axis, keepdims=True))

def mean_square_difference(x, query, axis=None):
    return np.sum((x-query)**2, axis =axis, keepdims=True)

def cosine_simility(x, query, axis=None):
    query_norm = np.sqrt(np.sum(query**2))
    x_norm = np.sqrt(np.sum(x**2, axis=axis, keepdims=True))
    return np.sum(x * query, axis=axis, keepdims=True) / (query_norm*x_norm)

def correlation_coeffiecient(x, query, axis=None):
    x_mean = np.mean(x, axis=axis, keepdims=True)
    query_mean = np.mean(query)
    return (
            np.sum((x - x_mean)*(query - query_mean), axis=axis, keepdims=True) / 
            np.sqrt(np.sum((x-x_mean)**2, axis=axis, keepdims=True)*np.sum((query - query_mean)**2))
            )


# In[147]:


def get_features():
    features =[]
    img_paths =[]
    root_img =  "static\img\\"
    for feature_path in Path("./feature").glob("**/*.npy"):
        try:
            features.append(np.load(feature_path))
            img_paths.append(root_img + str(feature_path).split('\\')[1] + ("\\" + feature_path.stem + ".jpg"))
            #if (feature_path.stem.find('(')) != -1: # remove some file "..(1).npy"
                #print(feature_path.stem)
                #os.remove(feature_path)
        except ValueError:
            print("error: ",feature_path)
            #os.remove(feature_path)
    features = np.array(features)
    return features, img_paths
#print(features)


# ![](https://cdn.educba.com/academy/wp-content/uploads/2019/06/Correlation-Coefficient-Formula.jpg)

# In[148]:





# In[153]:


def get_scores(file, features, img_paths):
    
    fe = FeatureExtractor()
    query = fe.extract(file)
    
    #dists = absolute_difference(features , query, axis = 1).flatten()
    dists = mean_square_difference(features , query, axis = 1).flatten()
    ids = np.argsort(dists)[:30] #top 30 result
    #print(ids)
    scores = [(dists[id], img_paths[id]) for id in ids]
    return scores
#print(scores)


# In[156]:


#scores[0][0]


# In[154]:


if __name__ == "__main__":
    query_path = r"D:\Coursena AI for everyone\AI_course_2021\Exercise_Phase2\Project_Image_Retrievel\casau.jpg"
    features, img_paths = get_features()
    file = Image.open(query_path)
    scores = get_scores(file)
    
    fig = plt.figure(figsize=(15, 15))
    columns = 5
    rows = 6
    for i, img_path in enumerate(scores,1):
        #print(i,img_path)
        #img = np.random.randint(10, size=(10,10))
        fig.add_subplot(rows, columns, i)
        plt.imshow(plt.imread(img_path[1]))
        plt.axis("off")
    plt.show()

    


# In[ ]:





# In[ ]:




