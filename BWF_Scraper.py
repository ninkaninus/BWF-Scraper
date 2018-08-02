from bs4 import BeautifulSoup
import requests
import os
import time

def_link = 'https://bwf.tournamentsoftware.com/ranking/category.aspx?id=18312&category=472&C472FOC=&ps=100&p=1'

page_response = requests.get(def_link, timeout=10)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

day_code = []

for option in page_content.find_all('option'):
    day_code.append('{}'.format(option['value'], option.text))

print('Todays code ' + day_code[0])
today_link = def_link[:60] + day_code[0] + def_link[65:]

links_ms = []
links_ws = []
links_md = []
links_wd = []
links_mixd = []

for i in range(1):
    link_cat = today_link[:75] + '472&C472' + today_link[83:]
    link_page1 = link_cat[:97] + '1'
    link_page2 = link_cat[:97] + '2'
    links_ms.append(link_page1)
    links_ms.append(link_page2)

for i in range(1):
    link_cat = today_link[:75] + '473&C473' + today_link[83:]
    link_page1 = link_cat[:97] + '1'
    link_page2 = link_cat[:97] + '2'
    links_ws.append(link_page1)
    links_ws.append(link_page2)

for i in range(1):
    link_cat = today_link[:75] + '474&C474' + today_link[83:]
    link_page1 = link_cat[:97] + '1'
    link_page2 = link_cat[:97] + '2'
    links_md.append(link_page1)
    links_md.append(link_page2)

for i in range(1):
    link_cat = today_link[:75] + '475&C475' + today_link[83:]
    link_page1 = link_cat[:97] + '1'
    link_page2 = link_cat[:97] + '2'
    links_wd.append(link_page1)
    links_wd.append(link_page2)

for i in range(1):
    link_cat = today_link[:75] + '476&C476' + today_link[83:]
    link_page1 = link_cat[:97] + '1'
    link_page2 = link_cat[:97] + '2'
    links_mixd.append(link_page1)
    links_mixd.append(link_page2)

# make dir
directory = os.getcwd()
directory = directory + '/output'
print('Checking output folder')
if not os.path.exists(directory):
    print('Output folder does not exist')
    os.makedirs(directory)
    print('Output folder created')
else:
    print('Output folder exist')

# open files
MS = open('output/MS.csv', 'wt')
WS = open('output/WS.csv', 'wt')
MD = open('output/MD.csv', 'wt')
WD = open('output/WD.csv', 'wt')
MIXD = open('output/MIXD.csv', 'wt')

# description to files
MS.write('Rank;Name;BWF_ID \n')
WS.write('Rank;Name;BWF_ID \n')
MD.write('Rank;Name1;Name2;BWF_ID1;BWF_ID2 \n')
WD.write('Rank;Name1;Name2;BWF_ID1;BWF_ID2 \n')
MIXD.write('Rank;Name1;Name2;BWF_ID1;BWF_ID2 \n')

time.sleep(5)

# Write MS to file
for links in links_ms:
    page_link = links
    # fetch the content from url
    page_response = requests.get(page_link, timeout=10)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")

    rank_nr = page_content.find_all('td', attrs={'class': 'rank'})
    name = page_content.find_all('span', attrs={'class', 'printonly flag'})
    memberID = page_content.find_all('a', attrs={'class': 'icon profile'})
    for x in range(100):
        MS.write(rank_nr[x].getText().encode('utf-8'))
        MS.write(';')
        MS.write(name[x].find_next_sibling().getText().encode('utf-8'))
        MS.write(';')
        MS.write(memberID[x].findNext('td').getText().encode('utf-8'))
        MS.write('\n')

print('MS written to file')

time.sleep(5)

# Write WS to file
for links in links_ws:
    page_link = links
    # fetch the content from url
    page_response = requests.get(page_link, timeout=10)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")

    rank_nr = page_content.find_all('td', attrs={'class': 'rank'})
    name = page_content.find_all('span', attrs={'class', 'printonly flag'})
    memberID = page_content.find_all('a', attrs={'class': 'icon profile'})
    for x in range(100):
        WS.write(rank_nr[x].getText().encode('utf-8'))
        WS.write(';')
        WS.write(name[x].find_next_sibling().getText().encode('utf-8'))
        WS.write(';')
        WS.write(memberID[x].findNext('td').getText().encode('utf-8'))
        WS.write('\n')

print('DS written to file')

time.sleep(5)

# Write MD to file
for links in links_md:
    page_link = links
    # fetch the content from url
    page_response = requests.get(page_link, timeout=10)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")

    rank_nr = page_content.find_all('td', attrs={'class': 'rank'})
    name = page_content.find_all('span', attrs={'class', 'printonly flag'})
    memberID = page_content.find_all('a', attrs={'class': 'icon profile'})
    for x in range(100):
        MD.write(rank_nr[x].getText().encode('utf-8'))
        MD.write(';')
        MD.write(name[x * 2].find_next_sibling().getText().encode('utf-8'))
        MD.write(';')
        MD.write(name[(x * 2) + 1].find_next_sibling().getText().encode('utf-8'))
        MD.write(';')
        MD.write(memberID[x * 2].findNext('td').findNext('p').getText().encode('utf-8'))
        MD.write(';')
        MD.write(memberID[x * 2].findNext('td').findNext('p').findNext('p').getText().encode('utf-8'))
        MD.write('\n')

print('MD written to file')

time.sleep(5)

# Write WD to file
for links in links_wd:
    page_link = links
    # fetch the content from url
    page_response = requests.get(page_link, timeout=10)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")

    rank_nr = page_content.find_all('td', attrs={'class': 'rank'})
    name = page_content.find_all('span', attrs={'class', 'printonly flag'})
    memberID = page_content.find_all('a', attrs={'class': 'icon profile'})
    for x in range(100):
        WD.write(rank_nr[x].getText().encode('utf-8'))
        WD.write(';')
        WD.write(name[x * 2].find_next_sibling().getText().encode('utf-8'))
        WD.write(';')
        WD.write(name[(x * 2) + 1].find_next_sibling().getText().encode('utf-8'))
        WD.write(';')
        WD.write(memberID[x * 2].findNext('td').findNext('p').getText().encode('utf-8'))
        WD.write(';')
        WD.write(memberID[x * 2].findNext('td').findNext('p').findNext('p').getText().encode('utf-8'))
        WD.write('\n')

print('WD written to file')

time.sleep(5)

# Write MIXD to file
for links in links_mixd:
    page_link = links
    # fetch the content from url
    page_response = requests.get(page_link, timeout=10)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")

    rank_nr = page_content.find_all('td', attrs={'class': 'rank'})
    name = page_content.find_all('span', attrs={'class', 'printonly flag'})
    memberID = page_content.find_all('a', attrs={'class': 'icon profile'})
    for x in range(100):
        MIXD.write(rank_nr[x].getText().encode('utf-8'))
        MIXD.write(';')
        MIXD.write(name[x * 2].find_next_sibling().getText().encode('utf-8'))
        MIXD.write(';')
        MIXD.write(name[(x * 2) + 1].find_next_sibling().getText().encode('utf-8'))
        MIXD.write(';')
        MIXD.write(memberID[x * 2].findNext('td').findNext('p').getText().encode('utf-8'))
        MIXD.write(';')
        MIXD.write(memberID[x * 2].findNext('td').findNext('p').findNext('p').getText().encode('utf-8'))
        MIXD.write('\n')

print('MIXD written to file')

MS.close()
WS.close()
MD.close()
WD.close()
MIXD.close()

print('Scraping complete')
