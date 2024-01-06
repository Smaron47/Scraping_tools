from bs4 import BeautifulSoup
import requests
import xlsxwriter
import time
from selenium import webdriver
browser = webdriver.Chrome("google-chorme")



re=requests.get("https://www.google.com/maps/place/Rainforest+Cafe/@23.6082426,89.8322107,15z/data=!4m9!1m2!2m1!1sRestaurants!3m5!1s0x39fe3ac0e6457505:0x725cd29837554e29!8m2!3d23.5989314!4d89.8354629!15sCgtSZXN0YXVyYW50c1oNIgtyZXN0YXVyYW50c5IBCnJlc3RhdXJhbnQ").text
a=re.find("Oasis Live Kitchen Restaurant & Cafe")
print(re)
'''
soup=BeautifulSoup(re)
print(soup)
soup=soup.find_all("a")

print(soup)
'''
workbook=xlsxwriter.Workbook("C:\\Users\\Manik Chandra Biswas\\Desktop\\excel fiel\\all links.xlsx")
worksheet=workbook.add_worksheet('linked2')
payel=0
row=1
col=1

for rea in range(1,2000):
    if rea==1457 or rea==1481 or rea==950:
        pass
    else:
        url=f"https://miningdataonline.com/property/{rea}/Copper-Mountain-Mine.aspx"
    
        k=requests.get(url).text
        soup=BeautifulSoup(k)

        l=soup.find(id="MainBody_gvDocuments")
        s=BeautifulSoup(str(l))

        u=soup.find(id="address")
        ad=BeautifulSoup(str(u))
        ad=ad.find('div')

        a=str(ad).find('<br/>')
        fuck=BeautifulSoup(str(ad)[a:a+100])
        e=str(fuck).split('<br/>')
        y=s.find_all('a')
        p=0
        for i in s.find_all('span'):
            span=i.get('class')
            ni=i.get('id').split('_')
            if span==None:
                dt=(i.get('id')).split('_')
                try:
                    o=y[p].get('id').split('_')
                    if dt[-1]==o[-1]:
                        #print(rea,y[p].text,i.text)
                        worksheet.write(row,col,rea)
                        worksheet.write(row,col+1,url)
                        worksheet.write(row,col+2,e[1])
                        worksheet.write(row,col+3,e[2])
                        worksheet.write(row,col+4,(y[p].text))
                        worksheet.write(row,col+5,(i.text))
                        worksheet.write(row,col+6,(y[p].get('href')))
                        row += 1
                        print(f"{rea} done..")
                        p=p+1
                    else:
                        worksheet.write(row,col,rea)
                        worksheet.write(row,col+1,url)
                        worksheet.write(row,col+2,e[1])
                        worksheet.write(row,col+3,e[2])
                        worksheet.write(row,col+4,".................")
                        worksheet.write(row,col+5,(i.text))
                        row += 1
                        print(f"{rea} done..")
                except:
                    pass
print("Writing on file")
workbook.close()
'''

import json
import re
from bs4 import BeautifulSoup
import requests
from ast import literal_eval




url="https://www.google.com/maps/place/Rainforest+Cafe/@23.5989314,89.8332689,17z/data=!3m1!4b1!4m5!3m4!1s0x39fe3ac0e6457505:0x725cd29837554e29!8m2!3d23.5989314!4d89.8354629"
url2="https://www.google.com/search?tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=AOaemvIHgcDu7bBKdxI55xu94-mFh6TBqw:1630260506518&q=restaurants+in+faridpur&rflfq=1&num=10&sa=X&ved=2ahUKEwik-obT6dbyAhXA_XMBHcCCA9kQjGp6BAgXEEw&biw=1279&bih=920#rlfi=hd:;si:;mv:[[23.604878,89.840666],[23.594971299999997,89.8272484]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9"
u="https://www.google.com/search?tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=AOaemvJZFAsJl6-f0nQ_pS9JUvyNIfXHvA:1630261361135&q=restaurants+in+faridpur&rflfq=1&num=10&sa=X&ved=2ahUKEwi8zMjq7NbyAhWTX3wKHRMnAgIQjGp6BAgXEEw#rlfi=hd:;si:;mv:[[23.610041840785996,89.86115479941101],[23.579956287154573,89.82429051871033]]"
req=requests.get("https://www.google.com/search?q=collages%20in%20faridpur&client=ms-android-samsung-ga-rev1&biw=1279&bih=920&tbm=lcl&sxsrf=AOaemvIncFGAPdvcW1C_BTd6GzewIJOYbA%3A1630261643085&ei=i9ErYazLBOLC3LUPmIuh0AY&oq=collages+in+faridpur&gs_l=psy-ab.3..0i13i5i30k1l2.453334.467457.0.467980.22.20.1.1.1.0.191.3102.0j19.19.0....0...1c.1.64.psy-ab..1.21.3106...35i39k1j0i273k1j0i512k1j0i512i433i131k1j0i512i433k1j0i433i67k1j0i67k1j0i433i273k1j0i433i10k1j0i10k1j0i457i10k1j0i402k1j33i10i160k1j0i22i30k1.0.uudcq2zg6HU&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rlst=f#rlfi=hd:;si:;mv:[[23.616623399999998,89.8774018],[23.538719399999998,89.7920516]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2").text
print(req)

s=BeautifulSoup(req)

print(s)'''