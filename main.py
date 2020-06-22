from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe (title , message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\User\Desktop\PROGRAMMING\PYTHON PROJECTS\Covid 19 Realtime Notificaton system\corona.ico",
        timeout = 8 ,
    )

def get_data_url (url):
     r  = requests.get(url)
     return r.text




if __name__ == "__main__":
    while True:
            
        # notifyMe("Harry" , "Let's stop this virus")
        myhtmldata = get_data_url("https://www.mohfw.gov.in/")

        mystr_data = ""

        soup = BeautifulSoup( myhtmldata , 'html.parser')

        for table in soup.find_all('tbody'):
            # print(table.get_text())
            mystr_data += table.get_text()

        new_list = mystr_data.split("\n\n")
        new_list = new_list[1:36]
        new_list[0] = new_list[0][1:]
        states = ['Maharashtra']
        for x in new_list:
            datalist = x.split("\n")[1:]
            if datalist[1] in states:
                notify_text = f"\nIN MAHARASHTRA:\nActive Cases of covid 19 is {datalist[2]}\nDischarged patients are {datalist[3]}\nDeaths are {datalist[4]}\nTotal Cases are {datalist[5]}"
        
        
        notifyMe("CASES of COVID 19 ", notify_text)
        time.sleep(10)


    