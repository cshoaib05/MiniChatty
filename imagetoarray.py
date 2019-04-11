import cv2
import numpy as np
import csv


img = cv2.imread('RIZWAN_data\\my_img314.png',0)
b = []
# img.resize(230,230)
for a in img:
	# print(a)
	b.append(str(a).replace('\n','').replace(']','').replace("',",'').replace(',',''))


bab=str(b).replace(',','').replace("'",'').replace("[",'')
print(len(bab))
data= bab.replace(' ',",")
# print(data)
imgdata=data.replace(",,",',')
# print(len(imgdata))
# css =  open('data.csv', 'a')
# # b=str(a).replace(']','').replace('[','').replace("'",'')
# # print(b)
# css.write(imgdata)
# css.write('\n')
# css.close()

# css =  open('data.csv', 'a')
# # b=str(a)
# css.write(imgdata)
# css.close()
