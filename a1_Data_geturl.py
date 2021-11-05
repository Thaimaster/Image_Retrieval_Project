#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf


# In[ ]:


#pip install selenium
#pip install wget


# In[1]:


from bs4 import BeautifulSoup # Parse HTML
from urllib.parse import urljoin, urlparse # check link
import urllib.request # download picture
import requests as rq
import threading # Multi Processing
import time


# In[2]:


#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from os import getcwd
import os


# #### Catagories & website
# 
# 

# In[3]:


dict_categories = {

"animal"  : ["Monkey",  "Elephant",  "cows",  
            "Cat",  "Dog",  "bear",  "fox",  "Civet", 
            "Pangolins", "Rabbit", "Bats", "Whale", 
            "Cock", "Owl", "flamingo", "Lizard", "Turtle", 
            "Snake", "Frog", "Fish", "shrimp", "Crab", "Snail", 
            "Coral", "Jellyfish", "Butterfly", "Flies", "Mosquito", 
            "Ants", "Cockroaches", "Spider", "scorpion", "tiger", 
            "bird",  "horse", "pig", "Alligator" ,"Alpaca" , 
            "Anteater", "donkey", "Bee", "Buffalo", "Camel", 
            "Caterpillar", "Cheetah", "Chicken",  "Dragonfly", 
            "Duck", "panda", "Giraffe"],

"plant" :["Bamboo", "Apple", "Apricot", "Banana", "Bean", 
            "Wildflower", "Flower", "Mushroom", "Weed", "Fern" , "Reed", 
            "Shrub", "Moss", "Grass", "Palm_tree", "Corn", "Tulip", "Rose",
            "Clove", "Dogwood", "Durian", "Ferns", "Fig", "Flax", "Frangipani", 
            "Lantana", "Hibiscus", "Bougainvillea", "Pea", "Orchid_Tree", "Rangoon_Creeper",
            "Jack_fruit", "Cotton_plant", "Cornelian_tree", "Coffee_plant", "Coconut"
            , "wheat", "watermelon", "radish", "carrot"],

"furniture" :["bed", "cabinet", "chair", "chests", "clock", 
            "desks", "table", "Piano", "Bookcase", "Umbrella", "Clothes", 
            "cart", "sofa", "ball", "spoon", "Bowl", "fridge", "pan", "book"],

"scenery" :["Cliff", "Bay", "Coast", "Mountains", "Forests", 
            "Waterbodies", "Lake", "desert", "farmland", "river", "hedges", 
            "plain", "sky", "cave", "cloud", "flower_garden", "glacier", 
            "grassland", "horizon", "lighthouse", "plateau", "savannah", "valley", "volcano", "waterfall"]
}


#for k, v in dict_categories.items():
#    for name in v:
#        print(name)


# In[4]:


# Static web
name='cat'
ipage = 2

web1 = f"https://pixabay.com/photos/search/{name}/"
web2 = f"https://www.pexels.com/search/{name}/"
web3 = f"https://www.freeimages.com/search/{name}/{ipage}"
web0 = f'https://ww|w.pinterest.com/search/pins/?q={name}'
name = 'dog'

web5 = f"https://www.freepik.com/search?from_query={name}&query={name}&sort=popular&type=photo&page="
web6 = f"https://www.freeimages.com/search/{name}/"


# In[5]:


from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

from urllib.error import HTTPError, URLError # check error
import socket

# In[6]:


os.getcwd()
#os.mkdir('test')
#os.chdir('test')

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# In[8]:


def get_all_images(url):
    """
    args:
        - link trang web chứa ảnh
    
    Returns:
        all image URLs on a single `url`
    """
    try:
        response = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
    except HTTPError as error:
        logging.error('Data not retrieved because %s\nURL: %s', error, url)
    except URLError as error:
        if isinstance(error.reason, socket.timeout):
            logging.error('socket timed out - URL %s', url)
        else:
            logging.error('some other error happened)
    soup = BeautifulSoup(response, "html.parser")
    urls = []
    
    # get link img
    for img in soup.find_all("img"):
        
        img_url = img.attrs.get("src")
        
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        
        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
        
    return urls

def get_all_image_dynamic_web(web):
    '''
    use for dymanic web
    return list image url
    '''
    driver = webdriver.Chrome()
    driver.get(web)
    
    # For dymanic web
    for i in range(10):
        for j in range(5):
            driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
            time.sleep(0.15)
        time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = []

    for item in soup.find_all('img'):
        if is_valid(item['src']):
            links.append(item['src'])
    driver.close()
    return links


# In[9]:


# get img to txt
def get_img_to_txt(url, params):
    k, name, desination_folder = params
    
    if os.path.isfile(desination_folder) == False:
        os.makedirs('img', exist_ok=True)
    
    result = get_all_images(url)
    result2 = list(set(result))

    print(f"\n{k}_{name}.txt add {len(result2)} images")
    strResult = '\n'.join(result2)

    with open(desination_folder + f"\\{k}_{name}.txt", "a") as f:
        f.write(strResult)
    


# In[ ]:

if _name_ == '__main__':
    '''
    # optimazation
    1- trả vể list xog mới ghi txt nên rất chậm
         -Giải pháp: lấy dc link nào ghi vào file txt luôn
    2 - multi threading use ThreadPoolExecutor
    3 - chưa kiểm tra trùng lặp bên trong file txt nếu chạy lần 2, có thể clean sau khi crawl text
    '''

    count = 0
    npage=6
    desination_folder = os.getcwd()
    list_param =[]
    urls = []
    start_time = time.time()

    #==========================
    for k, v in dict_categories.items():
        for name in v:
            
            params = list([k, name, desination_folder])
            
            for ipage in range(1,npage+1):
                list_param.append(params)
                # get  url follow catagories and npage
                url = f"https://www.freepik.com/search?dates=any&format=search&sort=popular&page={ipage}&query={name}"
                urls.append(url)
                
                #debug count +=1


            #print(urls)
    #print(list_param)
         
    #use multi threading for npage
    with ThreadPoolExecutor(max_workers=402) as p:
        try:
            future_tasks = p.map(get_img_to_txt, urls, list_param, timeout = 15)
        except concurrent.futures.TimeoutError:
            print("this thread take too long")
       
    print("Done...")
    #print(urls)
    #938
     #========================   
    print('total time get url: ', time.time() - start_time)


