import cv2
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



img = cv2.imread('RIZWAN_data/my_img7.png')   
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
plt.imshow(resized)

npimg = np.array(resized, dtype = 'int')
b = list(npimg.flat)
print(b)


head = []
for i in range(1, 13873):
    head.append("pixel"+str(i))
    
    
head.insert(0, 'label')

s = ""
for h in range(len(head)-1):
    s += head[h]+','  
    
s += head[h+1]
s += '\n'


csv = open('data.csv', "w", encoding="utf-8") 
csv.write(s)
csv.close()