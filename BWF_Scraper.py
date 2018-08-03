from bs4 import BeautifulSoup
import requests
import os
import io

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
MS = io.open('output/MS.csv', 'wt')
WS = io.open('output/WS.csv', 'wt')
MD = io.open('output/MD.csv', 'wt')
WD = io.open('output/WD.csv', 'wt')
MIXD = io.open('output/MIXD.csv', 'wt')

# description to files
MS.write(u'Rank;Name;BWF_ID;\n')
WS.write(u'Rank;Name;BWF_ID;\n')
MD.write(u'Rank;Name1;Name2;BWF_ID1;BWF_ID2;\n')
WD.write(u'Rank;Name1;Name2;BWF_ID1;BWF_ID2;\n')
MIXD.write(u'Rank;Name1;Name2;BWF_ID1;BWF_ID2;\n')

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
        MS.write(rank_nr[x].getText())
        MS.write(u';')
        MS.write(name[x].find_next_sibling().getText())
        MS.write(u';')
        MS.write(memberID[x].findNext('td').getText())
        MS.write(u';\n')

print('MS written to file')

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
        WS.write(rank_nr[x].getText())
        WS.write(u';')
        WS.write(name[x].find_next_sibling().getText())
        WS.write(u';')
        WS.write(memberID[x].findNext('td').getText())
        WS.write(u';\n')

print('DS written to file')

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
        MD.write(rank_nr[x].getText())
        MD.write(u';')
        MD.write(name[x * 2].find_next_sibling().getText())
        MD.write(u';')
        MD.write(name[(x * 2) + 1].find_next_sibling().getText())
        MD.write(u';')
        MD.write(memberID[x * 2].findNext('td').findNext('p').getText())
        MD.write(u';')
        MD.write(memberID[x * 2].findNext('td').findNext('p').findNext('p').getText())
        MD.write(u';\n')

print('MD written to file')

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
        WD.write(rank_nr[x].getText())
        WD.write(u';')
        WD.write(name[x * 2].find_next_sibling().getText())
        WD.write(u';')
        WD.write(name[(x * 2) + 1].find_next_sibling().getText())
        WD.write(u';')
        WD.write(memberID[x * 2].findNext('td').findNext('p').getText())
        WD.write(u';')
        WD.write(memberID[x * 2].findNext('td').findNext('p').findNext('p').getText())
        WD.write(u';\n')

print('WD written to file')

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
        MIXD.write(rank_nr[x].getText())
        MIXD.write(u';')
        MIXD.write(name[x * 2].find_next_sibling().getText())
        MIXD.write(u';')
        MIXD.write(name[(x * 2) + 1].find_next_sibling().getText())
        MIXD.write(u';')
        MIXD.write(memberID[x * 2].findNext('td').findNext('p').getText())
        MIXD.write(u';')
        MIXD.write(memberID[x * 2].findNext('td').findNext('p').findNext('p').getText())
        MIXD.write(u';\n')

print('MIXD written to file')

MS.close()
WS.close()
MD.close()
WD.close()
MIXD.close()

print('Scraping complete')
