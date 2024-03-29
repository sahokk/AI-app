import cv2
import datetime
import schedule
import time

deviceid=1 # it depends on the order of USB connection. 
capture = cv2.VideoCapture(deviceid)

def job():
    ret, frame = capture.read()
    strdate=datetime.datetime.now().strftime('%Y%m%dT%H%M%S') 
    fname="image_" + strdate + ".jpg"
    cv2.imwrite(fname, frame) 
    print(fname + " is created.")

#do job every 10 seconds
schedule.every(1/6).minutes.do(job)

while True:
  schedule.run_pending()
  time.sleep(1)