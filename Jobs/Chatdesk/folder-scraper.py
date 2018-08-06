import os
import sys
import csv
from itertools import izip_longest
from BeautifulSoup import BeautifulSoup

names = []
info = []
r_info = []
b_info = []
g_info = []
data = []

reload(sys)
sys.setdefaultencoding('utf8')
sys.setrecursionlimit(20000)

path = '/Users/franciscoruiz/Desktop/LinkedIn_1' # This is your folder name which stores all your html 
for filename in os.listdir(path): #Read files from your path
    #Getting the full path of a particular html file
        fullpath = os.path.join(path, filename)
        #If we have html tag, then read it
        if fullpath.endswith('.html'):
            #Then we will run beautifulsoup to extract the contents
            soup = BeautifulSoup(open(fullpath))
            # grabs each field
            #for y in soup.findAll('a', attrs={'class': 'name-link account-link'}): names.append(y.get('title'))

            for z in soup.findAll('span', attrs={'class': 'UFICommentBody'}): info.append(z.text)

def separate(index, listz):
    if len(listz) < 1: 
        return r_info
    elif listz[index].find("employees") != -1:
        r_info.append(listz[:1])
        b_info.append(listz[1:index])
        g_info.append(listz[index:index+1])
        del listz[:index+1]
        return separate(0,listz)
    else:
        return separate(index+1,listz)

#separate(0,info)

data.append(names)
data.append(r_info)
data.append(b_info)
data.append(g_info)

with open('linkedin.csv', 'a') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(['Name', 'Industry', 'Location', 'Size'])
    for data in izip_longest(*data):
        writer.writerow(data)