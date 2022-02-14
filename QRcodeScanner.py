#Assignment 10

#Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read

#Note: 
#	- Search how to generate QRCode
#	- Search how to read QRCode using webcam
#	- Search how to create and write to text file
#	- Your source code should be in github before Feb 19
#	- Create a demo of your program (1-2 min) and send it directly to my messenger

from encodings import utf_8
import cv2
from cv2 import putText
from pyzbar import pyzbar

def read_qrcodes(frame):
    qrcodes = pyzbar.decode(frame)
    for qrcode in qrcodes:
        x, y, w, h = qrcode.rect
        #Decode the qrcode
        qrcode_info = qrcode.data.decode('utf_8')
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0, 255, 0), 2)

        #Show the text
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2,putText(frame, qrcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        #Export into text document
        with open("QRcode_Result.txt", mode = 'w') as file:
            file.write("Recognized QR code:" + qrcode_info)
    return frame


