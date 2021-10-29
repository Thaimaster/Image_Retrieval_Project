#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import tensorflow as tf


# # In[1]:


# #pip install selenium
# #!pip install wget


# # In[2]:


# from bs4 import BeautifulSoup # Parse HTML
# from urllib.parse import urljoin, urlparse # check link
# import urllib.request # download picture
# import requests as rq
# import threading # Multi Processing
# import time


# # In[3]:


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from os import getcwd
# from concurrent.futures import ThreadPoolExecutor #Multi Threading

# import os


# # #### Catagories & website
# # 
# # 

# # In[4]:


# dict_categories = {

# "animal"  : ["Monkey",  "Elephant",  "cows",  
            # "Cat",  "Dog",  "bear",  "fox",  "Civet", 
            # "Pangolins", "Rabbit", "Bats", "Whale", 
            # "Cock", "Owl", "flamingo", "Lizard", "Turtle", 
            # "Snake", "Frog", "Fish", "shrimp", "Crab", "Snail", 
            # "Coral", "Jellyfish", "Butterfly", "Flies", "Mosquito", 
            # "Ants", "Cockroaches", "Spider", "scorpion", "tiger", 
            # "bird",  "horse", "pig", "Alligator" ,"Alpaca" , 
            # "Anteater", "donkey", "Bee", "Buffalo", "Camel", 
            # "Caterpillar", "Cheetah", "Chicken",  "Dragonfly", 
            # "Duck", "panda", "Giraffe"],

# "plant" :["Bamboo", "Apple", "Apricot", "Banana", "Bean", 
            # "Wildflower", "Flower", "Mushroom", "Weed", "Fern" , "Reed", 
            # "Shrub", "Moss", "Grass", "Palm_tree", "Corn", "Tulip", "Rose",
            # "Clove", "Dogwood", "Durian", "Ferns", "Fig", "Flax", "Frangipani", 
            # "Lantana", "Hibiscus", "Bougainvillea", "Pea", "Orchid_Tree", "Rangoon_Creeper",
            # "Jack_fruit", "Cotton_plant", "Cornelian_tree", "Coffee_plant", "Coconut"
            # , "wheat", "watermelon", "radish", "carrot"],

# "furniture" :["bed", "cabinet", "chair", "chests", "clock", 
            # "desks", "table", "Piano", "Bookcase", "Umbrella", "Clothes", 
            # "cart", "sofa", "ball", "spoon", "Bowl", "fridge", "pan", "book"],

# "scenery" :["Cliff", "Bay", "Coast", "Mountains", "Forests", 
            # "Waterbodies", "Lake", "desert", "farmland", "river", "hedges", 
            # "plain", "sky", "cave", "cloud", "flower_garden", "glacier", 
            # "grassland", "horizon", "lighthouse", "plateau", "savannah", "valley", "volcano", "waterfall"]
# }


# #for k, v in dict_categories.items():
# #    for name in v:
# #        print(name)


# # In[5]:


# # Static web
# name='cat'
# ipage = 2

# web1 = f"https://pixabay.com/photos/search/{name}/"
# web2 = f"https://www.pexels.com/search/{name}/"
# web3 = f"https://www.freeimages.com/search/{name}/{ipage}"
# web0 = f'https://ww|w.pinterest.com/search/pins/?q={name}'
# name = 'dog'

# web5 = f"https://www.freepik.com/search?from_query={name}&query={name}&sort=popular&type=photo&page="
# web6 = f"https://www.freeimages.com/search/{name}/"


# # In[6]:





# # In[7]:


# os.getcwd()
# #os.mkdir('test')
# #os.chdir('test')


# # In[ ]:





# # In[ ]:





# # In[ ]:


# # test multi threading
# #name = 'monkey'
# #k= 'animal'
# #desination_folder = os.getcwd()+ f"\img\\"
# #params = list([k, name, desination_folder])
# #url = f"https://www.freepik.com/search?from_query={name}&query={name}&sort=popular&type=photo&page={npage}"

# #start_time = time.time()

# #==========================


# #with ThreadPoolExecutor(max_workers=4) as p:
# #    p.map(get_all_images(links))

 # #========================   
# #print('total time:', time.time() - start_time)


# # In[8]:


# def is_valid(url):
    # """
    # Checks whether `url` is a valid URL.
    # """
    # parsed = urlparse(url)
    # return bool(parsed.netloc) and bool(parsed.scheme)


# # In[9]:


# def get_all_images(url):
    # """
    # args:
        # - link trang web chứa ảnh
    
    # Returns:
        # all image URLs on a single `url`
    # """
    # soup = BeautifulSoup(urllib.request.urlopen(url), "html.parser")
    # urls = []
    
    # # get link img
    # for img in soup.find_all("img"):
        
        # img_url = img.attrs.get("src")
        
        # if not img_url:
            # # if img does not contain src attribute, just skip
            # continue
        
        # # make the URL absolute by joining domain with the URL that is just extracted
        # img_url = urljoin(url, img_url)
        # # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        # try:
            # pos = img_url.index("?")
            # img_url = img_url[:pos]
        # except ValueError:
            # pass
        
        # # finally, if the url is valid
        # if is_valid(img_url):
            # urls.append(img_url)
        
    # return urls

# def get_all_image_dynamic_web(web):
    # '''
    # use for dymanic web
    # return list image url
    # '''
    # driver = webdriver.Chrome()
    # driver.get(web)
    
    # # For dymanic web
    # for i in range(10):
        # for j in range(5):
            # driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
            # time.sleep(0.15)
        # time.sleep(0.5)

    # soup = BeautifulSoup(driver.page_source, "html.parser")
    # links = []

    # for item in soup.find_all('img'):
        # if is_valid(item['src']):
            # links.append(item['src'])
    # driver.close()
    # return links


# # In[13]:


# # get img to txt
# def get_img_to_txt(url, params):
    # k, name, desination_folder = params
    
    # if os.path.isfile(desination_folder) == False:
        # os.makedirs('img', exist_ok=True)
    
    # result = get_all_images(url)
    # result2 = list(set(result))

    # print(f"\n{k}_{name}.txt add {len(result2)} images")
    # strResult = '\n'.join(result2)

    # with open(desination_folder + f"{k}_{name}.txt", "a") as f:
        # f.write(strResult)
    


# # In[12]:


# '''
# # optimazation
# 1- trả vể list xog mới ghi txt nên rất chậm
     # -Giải pháp: lấy dc link nào ghi vào file txt luôn
# 2 - multi threading use ThreadPoolExecutor
# 3 - chưa kiểm tra trùng lặp bên trong file txt nếu chạy lần 2
# '''

# count = 0
# npage=6
# desination_folder = os.getcwd()
# list_param =[]
# urls = []
# start_time = time.time()

# #==========================
# for k, v in dict_categories.items():
    # for name in v:
        
        # params = list([k, name, desination_folder])
        
        # for ipage in range(1,npage+1):
            # list_param.append(params)
            # # get  url follow catagories and npage
            # url = f"https://www.freepik.com/search?dates=any&format=search&sort=popular&page={ipage}&query={name}"
            # urls.append(url)
            
            # #debug count +=1


        # #print(urls)
# #print(list_param)
        
# #use multi threading for npage
# with ThreadPoolExecutor(max_workers=600) as p:
    # p.map(get_img_to_txt, urls, list_param)           
# #print(urls)
# #938
 # #========================   
# print('total time:', time.time() - start_time)


# In[58]:


import wget
import threading
import time
import requests
import urllib.request, urllib.error
import random
import os


# In[59]:


from concurrent.futures import ThreadPoolExecutor


# In[52]:


# # -*- coding: utf-8 -*-
# """
# Created on Mon Mar 22 15:37:46 2021

# @author: Quang Van
# """

# import wget
# import threading
# import time
# import requests
# import urllib.request, urllib.error
# import random
# import os

# class DownloadFromUrl():
    # def __init__(self, nThreads, urls, destinate_folder):
        # self.nThreads = nThreads
        # self.urls = urls
        # self.n = len(urls)
        # self.destinate_folder = destinate_folder
    
    # #===== util ===
    # def get_url_status(self, url):  # checks status for each url in list urls
        # try:
            # urllib.request.urlopen(url)
            # requests.get(url)
        # except Exception as e:
            # return False
        # else:
            # return True
        
    # # Func target
    # def down_url(self, start, end):

        # for i in range(start, end):
            # try:
                # response=requests.get(self.urls[i])
            # except Exception as e:
                # continue
            
            # # Tránh trùng tên
            # a = random.random()
            # with open(f"{self.destinate_folder}/{a}.jpg", "wb") as f:
                # f.write(response.content)
            # print('.', end=" ")         
                 
    # def __call__(self):
        # try:
            
            # threads = []
            
            # #=================
            # batch = self.n//self.nThreads
            # for i in range(0, self.n, batch):
                # start = i
                # end = i + batch

                # if end >= self.n:
                    # end = self.n + 1

                # threads.append(threading.Thread(target=self.down_url, args = (start, end)))
        
            # #=================
            # for i in range(self.nThreads):
                # threads[i].start()
            # for i in range(self.nThreads):
                # threads[i].join()

        # except Exception as e:
            # pass    
       
    # def __str__(self):
        # return f"Excute with {self.nThreads} Thread = {self.ExcuteThread} s\n"
    
    


# In[53]:

# In[54]:


#os.getcwd()


# In[55]:



def checkurl(url):
    try:
        response = urllib.request.urlopen(url, timeout=3)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        return False
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        return False
    except socket.timeout as e:
        print('socket timeout: ', url)
        return False
    else:
        #print ('Website is working fine')
        return True


# In[54]:


#os.getcwd()


# In[55]:


def download_img_url(url, params):
    destination_folder = params
    #count += 1
    if checkurl(url):
        try:
            response=requests.get(url)
        except Exception as e:
            print("link error: ",url)
        #time.sleep(1)
        # Tránh trùng tên
        a = random.random()
        with open(f"{destination_folder}\\{a}.jpg", "wb") as f:
            f.write(response.content)
        print('* ', end="", flush=True)   


# In[51]:


#url = "https://img.freepik.com/free-photo/little-rabbit_72229-1213.jpg"
#params = "D:\\Coursena AI for everyone\\AI_course_2021\\Exercise_Phase2\\Project_Image_Retrievel\\img\\animal_Rabbit" 


# In[56]:

if _name_ == '__main__':
    l = []
    for name_txt in os.listdir():
        if name_txt.endswith(".txt"):
            l.append(name_txt)


    # In[57]:



    # setup iterable
    list_folders =[]
    list_urls = []
    # setup destination folder
    root = os.getcwd()
    path = root + f"\img" 
    for name_txt in l:
        try:
            #print(f"\n {name_txt}")
            with open(root + f"\\{name_txt}", "r") as f:
                content = f.readlines()

            content = [x.strip() for x in content] 
            path = root + f"\img" +f"\\{name_txt[:-4]}"
            os.makedirs(path , exist_ok=True)
            list_urls.extend(content)
            
            for i in range (len(content)):
                list_folders.append(path)

        except Exception:
            pass

    print('total task:',len(list_folders))
    # In[45]:


    #len(list_urls)


    # In[61]:


    #print(list_folders[293:310])


    # In[ ]:


    #Multi downloading
    '''
    Stuck some thread, program cant run complete
    '''
    start_time = time.time()
    #===========================
    #count = 0
    with ThreadPoolExecutor(max_workers = 2741) as p: #1000
        p.map(download_img_url, list_urls, list_folders)
    #===========================
    print('Total download image time: ', time.time() - start_time)
