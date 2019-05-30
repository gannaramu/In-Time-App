#Importing packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from threading import Timer
from plyer import notification

f=open("userpass.txt")
data = f.read()
data = data.split("\n")
user = data[0]
passw = data[1]
f.close()
# Starting Chrome Driver and running it in background
options = webdriver.ChromeOptions();
options.add_argument('headless');  # To make it run in background
options.add_argument("--window-size=1920,1080") #Set screen size to extract most information from the table
options.add_argument("--start-maximized");
driver = webdriver.Chrome(chrome_options=options)

url='https://myworld.kpit.com/'
url_attendance='https://myworld.kpit.com/#/attendance'
driver.get(url)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userNameInput')))
except TimeoutException:
    print("Loading took too much time!")

username = driver.find_element_by_id("userNameInput")
password = driver.find_element_by_id("passwordInput")

username.send_keys(user)
password.send_keys(passw)

driver.find_element_by_id("submitButton").click() 
time.sleep(3)
driver.get(url_attendance)

try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'attendance_titles')))
except TimeoutException:
    print("Loading took too much time!")

tableProducts =   driver.find_element_by_id('attendance_titles')

table_text  = tableProducts.text
table_text  = table_text.split("\n")
In_Time_row = table_text[3]
In_Time_row   =  In_Time_row.split()
latest_in_time = In_Time_row[-1]

#tableRows     =   tableProducts.find_elements_by_tag_name('tr')
##tableColums   =  driver.find_elements_by_tag_name('td')
#In_Time_row   =  tableRows[2].text
#In_Time_row   =  In_Time_row.split()
#latest_in_time = In_Time_row[-1]

driver.close()
driver.quit()
from datetime import datetime, timedelta

datetime_object = datetime.strptime(latest_in_time,'%I:%M')
x = datetime.today()

latest_in_time_str    =  datetime_object.strftime('%I.%M %p')
expected_time     =  (datetime_object + timedelta(hours=9))
expected_time     =   expected_time.replace(year=x.year, month=x.month, day= x.day)
expected_time_str =  expected_time.strftime('%I.%M %p' )
import os.path
from os import path
folder = 'C:/Software/Attendance'


import os, shutil

if not(os.path.isdir(folder)):
    os.mkdir(folder)
	
for the_file in os.listdir(folder):
    file_path = os.path.join(folder+'/', the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

time.sleep(0.2)

    # define the name of the directory to be created
try:  
    os.mkdir(folder + '/' + 'In-' + latest_in_time_str)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)
time.sleep(0.2)

try:  
    os.mkdir(folder + '/' + 'Out_Exp-' + expected_time_str)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)

x = datetime.today()
y = expected_time

delta_t = y-x

secs=delta_t.seconds()


notification.notify(
    title='In-Time is ' + datetime_object.strftime('%I:%M %p'),
    message='This data is based on the latest available data from MyWorld',
    app_name='In Time App',
    app_icon='Time3.ico'
)

time.sleep(60)

 
def Notify():
    from plyer import notification
        
    notification.notify(
        title='9 hours Completed',
        message='You have successfully completed 9hrs for the day',
        app_name='In Time App',
        app_icon='Time3.ico'
    )

Notify()


t = Timer(secs, Notify)
t.start()

exit()
