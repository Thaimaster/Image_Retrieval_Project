from Feature_Extractor import FeatureExtractor
from pathlib import Path
import numpy as np
from PIL import Image
import os 
import matplotlib.pyplot as plt
import faiss
import time
import cv2

def load_data_trained():
    all_features_dir = "all_imgs_crop_features.npz"
    data = np.load(all_features_dir)
    features = data['array1']
    img_paths = data['array2']
    
    index = faiss.deserialize_index(np.load("index.npy"))
    
    #param
    index.nprobe = 10
    return features, img_paths, index
 
def load_index():
    index = faiss.deserialize_index(np.load("index.npy"))
    #param
    index.nprobe = 10
    return index
    
def main():
    
    features, img_paths, index = load_data_trained()

    if index.is_trained:
        ## number find cell
        
        xq = features[9571].reshape(1,-1)
        k=20
        dist, I = index.search(xq, k)
        
        #visualize
        columns = 5
        rows = 4
        fig = plt.figure(figsize=(15, 15))
        for i, id in enumerate(I[0],1):
            
            fig.add_subplot(rows, columns, i)
            print(img_paths[id])
            try:
                plt.axis("off")
                img = plt.imread(img_paths[id])
                plt.imshow(img)
                #plt.axis("off")
            except Exception:
                pass
        plt.show()
        
if __name__ == '__main__':
    main()
    
    
    

    