#!/usr/bin/env python
# coding: utf-8


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
