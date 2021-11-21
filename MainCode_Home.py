import serial, time
import urllib.request
import smtplib
from email.message import EmailMessage



def SerialCommWrite(num):
    global ser
    ser.write(num.encode())

def SerialCommRead():
    global ser
    if ser.in_waiting>0:
        Val=ser.readline().decode("ascii").rstrip()
        return Val
    
def SendEmail(opt):
    Sender_Email = "aryanbagoria30@gmail.com"
    Reciever_Email = "aryanbagoria12@gmail.com"
    Password = "arduinoproject"

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Emergency Message From Home" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    if opt==1:
        newMessage.set_content('Gas Leakage Occur')
    elif opt==2:
        newMessage.set_content('Person/motion Detected')
                           
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)


# Main Code
ser=serial.Serial('/dev/ttyACM0',9600)
ser.flush()

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
print("Starting System...")

while True:
    LinkR='https://techpacsrobo.000webhostapp.com/IOT/getdevice.php'
    RspR=urllib.request.urlopen(LinkR)
    Data=str(RspR.read())
    Ind=Data.find("#")
    Comnd=Data[Ind+1]
    if Comnd=="F":
        print("Fan")
        GPIO.output(23, GPIO.LOW) # out 
    elif Comnd=="L":
        print("Light")
        GPIO.output(24, GPIO.LOW)
        Ncmnd='L'
    elif Comnd=="1":
        print("Off F")
        GPIO.output(23, GPIO.HIGH)
    elif Comnd=="2":
        GPIO.output(24, GPIO.HIGH)
        print("Off L")
    elif Comnd=="R":
        SerialCommWrite("1")
        print("On L2")
    elif Comnd=="3":
        SerialCommWrite("2")
        print("Off L2")
    
    Val=SerialCommRead()
    if str(Val)!="None":
        if Val=="G":
            SendEmail(1)
            print("Email Sent For Gas")
        elif Val=="P":
            SendEmail(2)
            print("Email Sent For Motion")
  
    time.sleep(1)