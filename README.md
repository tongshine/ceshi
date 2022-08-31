# 使用说明
1. 添加链接：url = 'https://www.umei.cc/bizhitupian/fengjingbizhi/'
2. 导入BeautifulSoup： main_page = BeautifulSoup(resp.text, "html.parser")
3. find函数定位：alist=main_page.find("div", class_="swiper-wrapper after").find_all("a")
4. 在列表中遍历和标题
6. 写入文件：    
7. with open("imge/"+imge_name,mode = "wb") as f:
   f.write(down_resp.content)
