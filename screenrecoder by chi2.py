import cv2
from PIL import ImageGrab
import numpy as np
from numpr.core.arrayprint import array2string
import GetSystemMertics
import time

width=GetSystemMetrix(0)
height=GetSystemMetrix(1)

#===file_name===
file_name=f"video/Video_{str.(time.strftime('%d-%m-%Y %H_%S'))}.mp4"
"
fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
capture_video=vc2.videowriter(file_name,fourcc,20.0,(width,height))

while True:
	screen_img=ImageGrab.grab(bbox=(0,0,width,height))
	array_img=np.array(screen_img)
	color_img=cv2.cvtColor(array_img.cv2.COLOR_BRIGHTNES)
	capture_video.write(color_img)
	cv2.iamshow('chi screenrecodeer',color_img)
	if cv2.waitkey(1)==ord('q')
		break
											

