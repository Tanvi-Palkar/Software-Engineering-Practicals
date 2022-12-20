#CA Program no:1
#Sending and generating OTP as a program without Functional decomposition

import random
import smtplib

mailid = input("\nEnter Your Email Address : ")


otp = random.randint(1000,9999)
#print(otp)

server = smtplib.SMTP('smtp.gmail.com',587)


server.starttls()
#password obtained after doing two step verification on google account
password ="ifzf chii aafz jpgy"
server.login('palkartanvi216@gmail.com',password)

msg = 'Hello, Your OTP is ' + str(otp)

server.sendmail('palkartanvi216@gmail.com', mailid , msg)
print("OTP SEND !!")
server.quit()
