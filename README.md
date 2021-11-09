# **IMAGE RETRIEVAL**
---
## DEMO
[![Image Retrival Demo](screenshots/Screenshot1.jpg)](https://youtu.be/qcoXDGlA_qU)
---
## ALGORITHMS
 - Gather database:
    - Crawl image url from static web: 
    - Download image from url adn save to specific folder
    - Pre-processing image: remove invalid image
 - Main system:
    - Use saliency model to crop image from database then get feature extracting by VGG16 model. The query image will extract feature too.
    - In order to find similar image, I use Faiss (library search from Facebook). It use Euclidean method and IVFPQ ( Inverted Index + Product Quantization) to reduce memory and increase speed search
    - Finally, I use simple template web to implement and foward by ngrok
---
## REQUIREMENT
 - This package requires Python >= 3.7. Install all dependencies using requirements file:

   ` pip -r install requirement.txt`
- Download Dataset (required uncompressed program in direct path like: Winrar, 7Zip):
 `python Download_dataset.py` 
---
## RUN THE PROJECT
    python Sever.py
---
## Reference
- In this project, we use code from:
    - Saliency Prediction: https://github.com/alexanderkroner/saliency
- Document: 
    - Faiss search engine: https://faiss.ai/
