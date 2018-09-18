from urllib.request import urlopen
from bs4 import BeautifulSoup
url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/4/-1/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_page = raw_data.decode("utf-8")

f_conn = open('vinamilk.html','wb')
f_conn.write(raw_data)
f_conn.close()



soup = BeautifulSoup(html_page, "html.parser")
table = soup.find('table', id="tableContent")


tr_list = table.find_all('tr')

tr = tr_list[0]
td_list = tr.find_all('td')
menu_list = ['Category', 'Quy 1/2017', 'Quy 2/2017','Quy 3/2017','Quy 4/2017']



# songs_list =[]

# for tr in tr_list:

#     title = li.h3.string
#     link = li.a['href']
#     song = {
#         "Title": title,
#         "Link": link,
#     }
#     songs_list.append(song)


# import pyexcel
# pyexcel.save_as(records = songs_list, dest_file_name = 'itunes.xlsx')
