"""
批量图片url地址下载到本地保存
"""

import requests
import os

imgs = []
with open(r"D:\Users\Personal\Desktop\Work\ecc-bak-img.txt", 'r') as urls:
    for url in urls.readlines():
        r = requests.get(url.strip())
        file = r"D:\Users\Personal\Desktop\images\%s" % os.path.basename(url).strip()
        print(file)
        # break
        try:
            with open(file,"wb") as f:
                f.write(r.content)
        except:
            continue
        # print(os.path.basename(url))
# image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
# r = requests.get(image_url) 
# with open("python_logo.png",'wb') as f:
#     f.write(r.content)