import time

import requests
from bs4 import BeautifulSoup
url = 'https://www.umei.cc/bizhitupian/fengjingbizhi/'
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
alist=main_page.find("div", class_="swiper-wrapper after").find_all("a")
# print(alist)
for a in alist:
    herf = a.get('href')

    herf = 'https://www.umei.cc'+ herf
    # print(herf)
    child_resp = requests.get(herf)
    child_resp.encoding= 'utf-8'
    child_page = BeautifulSoup(child_resp.text, "html.parser")
    img= child_alist=child_page.find("div", class_="content-box").find("img")
    # print(img.get("src"))
    down_url =img.get("src")
    down_resp = requests.get(down_url)
    down_resp.content
    imge_name = down_url.split("/")[-1]
    with open("imge/"+imge_name,mode = "wb") as f:
        f.write(down_resp.content)
    print("over!", imge_name)
    time.sleep(1)
print("all over!!!")