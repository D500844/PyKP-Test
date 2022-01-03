import pandas as pd
from bs4 import BeautifulSoup
#PyKP Html->Excel
#12/9/2020

#Copy the html div based file you want scraped 
html = open(r"C:/Users/d5008/OneDrive/Desktop/PyKP/06_12_2020.html").read()

soup = BeautifulSoup(html, 'html.parser')

#Search for data types by div class names
Pname = soup.find_all('div', class_ = 'divPlayer')
Pdkp = soup.find_all('div', class_ = 'divDKP')
Pname_list = []
Pdkp_list = []

#Creating text lists out of scraped data
for item in Pdkp:
    Pdkp_list.append(item.text)
for item in Pname:
    Pname_list.append(item.text)

#Building an array and datatable
Final_Array = []

for Playername, Playerdkp in zip(Pname_list, Pdkp_list):
    Final_Array.append({'Player': Playername,'06/12/2020':Playerdkp})
    
data = pd.DataFrame(Final_Array)

data = data.style.hide_index()

datatoexcel = pd.ExcelWriter("WowPyKPtest2_1.xlsx",engine='xlsxwriter')

data.to_excel(datatoexcel, sheet_name='Sheet1')

datatoexcel.save()
#data





