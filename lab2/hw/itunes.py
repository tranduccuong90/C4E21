#Section 1
from urllib.request import urlopen
from bs4 import BeautifulSoup
url ="https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()
html_page = raw_data.decode("utf-8")
soup = BeautifulSoup(html_page, "html.parser")
section = soup.find('section', 'section chart-grid')


li_list = section.div.ul.find_all('li')
# print(li_list[0])

songs_list =[]

for li in li_list:

    title = li.h3.string
    link = li.a['href']
    artist = li.h4.string
    song = {
        "Title": title,
        "Link": link,
        "Artist": artist,
    }
    songs_list.append(song)


import pyexcel
pyexcel.save_as(records = songs_list, dest_file_name = 'itunes.xlsx')


#Section 2
from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)

#Concentrate Title and Artist into 1 string
songs_list_new = []
for song in songs_list:
    song_new = song['Title'] + ' ' + song['Artist']
    songs_list_new.append(song_new)

dl.download(songs_list_new)
