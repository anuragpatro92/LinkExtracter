from bs4 import BeautifulSoup
import numpy as np
import csv
num  = 1
with open("test.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    attr = { 'class':'title-link__1ay5'}
    len = len(soup.find_all('a',attr,href=True))
    shape = (len,2)
    data = list()
    for a in soup.find_all('a',attr ,href=True):
        temp = a['href']

        if(temp.startswith('https')):
            data.append(temp)
        elif(temp.startswith('/discuss')):
            str = 'https://leetcode.com'
            str = str + a['href']
            data.append(str)

    with open('data.csv', 'w+', newline='') as student_file:
        writer = csv.writer(student_file)
        for info in data:
            temp = list()
            temp.append(info)
            writer.writerow(temp)



