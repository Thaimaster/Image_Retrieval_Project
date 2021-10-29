#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


animal  =  ["Monkey",  "Elephant",  "cows",  
"Cat",  "Dog",  "bear",  "fox",  "Civet", 
"Pangolins", "Rabbit", "Bats", "Whale", 
"Cock", "Owl", "flamingo", "Lizard", "Turtle", 
"Snake", "Frog", "Fish", "shrimp", "Crab", "Snail", 
"Coral", "Jellyfish", "Butterfly", "Flies", "Mosquito", 
"Ants", "Cockroaches", "Spider", "scorpion", "tiger", 
"bird",  "horse", "pig", "Alligator" ,"Alpaca" , 
"Anteater", "donkey", "Bee", "Buffalo", "Camel", 
"Caterpillar", "Cheetah", "Chicken",  "Dragonfly", 
"Duck", "panda", "Giraffe"]

plant = ["Bamboo", "Apple", "Apricot", "Banana", "Bean", 
"Wildflower", "Flower", "Mushroom", "Weed", "Fern" , "Reed", 
"Shrub", "Moss", "Grass", "Palm_tree", "Corn", "Tulip", "Rose",
"Clove", "Dogwood", "Durian", "Ferns", "Fig", "Flax", "Frangipani", 
"Lantana", "Hibiscus", "Bougainvillea", "Pea", "Orchid_Tree", "Rangoon_Creeper",
"Jack_fruit", "Cotton_plant", "Cornelian_tree", "Coffee_plant", "Coconut"
, "wheat", "watermelon", "radish", "carrot"]

furniture = ["bed", "cabinet", "chair", "chests", "clock", 
"desks", "table", "Piano", "Bookcase", "Umbrella", "Clothes", 
"cart", "sofa", "ball", "spoon", "Bowl", "fridge", "pan", "book"]

scenery = ["Cliff", "Bay", "Coast", "Mountains", "Forests", 
"Waterbodies", "Lake", "desert", "farmland", "river", "hedges", 
"plain", "sky", "cave", "cloud", "flower_garden", "glacier", 
"grassland", "horizon", "lighthouse", "plateau", "savannah", "valley", "volcano", "waterfall"]


# In[3]:


dic_categories = {'animal':animal, 'plant':plant, 'furniture': furniture, 'scenery':scenery}


# In[4]:

# export categories by pandas
# # make all items to same length
# m = max([len(dic_categories[d]) for d in dic_categories])
# print(m)
# for d in dic_categories:
    # n = len(dic_categories[d])
    # dic_categories[d].extend((m - n)*[""])


# # In[5]:


# import pandas as pd
# df = pd.DataFrame(dic_categories)


# # In[6]:


# df


# # In[10]:


# df.to_csv("categories.csv", index=False)


# ## Pre_Processing

# In[80]:


import os 
from PIL import Image 
import numpy as np 
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import time


# In[81]:



#dic_categories = ['scenery', 'furniture', 'animal', 'plant'] 



# In[82]:


#os.listdir('img')
os.makedirs('img', exist_ok=True)
#os.getcwd()


# In[83]:





# In[66]:

def get_img_path():
    root = 'img/'
    dic_categories = ['scenery', 'furniture', 'animal', 'plant']
    
    img_paths =[]
    for folder in os.listdir(root):
        if folder.split("_")[0] in dic_categories:
    
            path = root + folder
            list_dir = [path + '/' + name for name in os.listdir(path)]
            img_paths.extend(list_dir)
    return img_paths
#print(img_paths)


# In[78]:


def preprocessing_img(img_paths):
    
    p = img_paths
    #print(p)
    try:
        if (p.endswith((".jpg", ".png", ".jpeg")))==False:
            print('not image: ',p)
            #os.remove(p)

        # ảnh lỗi hoặc ảnh không mở được...
        img = Image.open(p) # open the image file

        # size nhỏ quả
        if img.width < 10:
            print("Image too small: ", p)
            os.remove(p) # chú ý chỗ này, mới đầu chạy phải comment lại không lỡ lỗi mất hết ảnh
        # loại bỏ size lớn
        if img.width > 1600:
            print("Image too large: ", p)
            os.remove(p) # chú ý chỗ này, mới đầu chạy phải comment lại không lỡ lỗi mất hết ảnh
        #img = img.resize((224, 224))
        # lỗi không xác đinh
        img.verify() # verify that it is, in fact an image
        img.save(p)

    except Exception:
        #count += 1 #debug
        print("error: ", p, flush = True)
        #os.remove(p) # chú ý chỗ này, mới đầu chạy phải comment lại không lỡ lỗi mất hết ảnh
#preprocessing_img(img_paths[0])


# In[79]:


if __name__ == '__main__':
    img_paths = get_img_path()
    print(len(img_paths))
    
    
    #multi threading
    start_time = time.time()
    #===========================
    #preprocessing_img(img_paths[1])
    
    with ThreadPoolExecutor(max_workers=2741) as t:
        t.map(preprocessing_img, img_paths)
    #===========================
    print('Total processed image time: ', time.time() - start_time)
