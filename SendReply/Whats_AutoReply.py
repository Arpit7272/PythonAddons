import pywhatkit
import time
import re
from urllib.parse import quote
import webbrowser as web
import pyautogui as pg

dict=""
sleeptm = "None, You can use this function to print the remaining time in seconds."


def prnt_sleeptm():
    return sleeptm

def SendReply(number,text,time):
	global dict
	pat=re.compile(r'^[6-9]{1}[0-9]{9}$')
	try:
		if re.search(pat,number):
			num = "+91" + str(number)
			t=list(map(int,time.split(':')))
			#print(t)
			error=pywhatkit.sendwhatmsg(num,text,t[0],t[1])
			return dict,error
	except:
		return "Please fill the Details Correctly"

def sendwhatmsg(phone_no, message, time_hour, time_min, wait_time=20, print_waitTime=True):
    '''Sends whatsapp message to a particulal number at given time
		Phone number should be in string format not int
		***This function will not work if the browser's window is minimised,
		first check it by calling 'check_window()' function'''
    global sleeptm,dict
	
    # if "+" not in phone_no:
    #     raise CountryCodeException("Country code missing from phone_no")
    timehr = time_hour

    # if time_hour not in range(0,25) or time_min not in range(0,60):
        # print("Invalid time format")
    
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)
    
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm

    if lefttm < wait_time:
        return "Call time must be greater than wait_time as web.whatsapp.com takes some time to load"
    
    date = "%s:%s:%s"%(curr.tm_mday,curr.tm_mon,curr.tm_year)
    time_write = "%s:%s"%(timehr,time_min)
    # file = open("pywhatkit_dbs.txt","a",encoding='utf-8')
    # file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s"%(date,time_write,phone_no,message))
    # file.write("\n--------------------\n")
    # file.close()
    sleeptm = lefttm-wait_time
    if print_waitTime :
        dict= "In {prnt_sleeptm()} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered"
    time.sleep(sleeptm)
    parsedMessage = quote(message)
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(wait_time-2)
    pg.press('enter')


