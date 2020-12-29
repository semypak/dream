import requests
from bs4 import BeautifulSoup
url = "https://search.daum.net/search?w=tot&DA=LOT&rtmaxcoll=LOT&&q="+str()
req = requests.get(url)

if req.status_code != requests.codes.ok:
    print("접속실패")
    exit()
html = BeautifulSoup(req.text, "html.parser")
numbers = html.select(".img_lotto")
for number in numbers :
    print(number)


# custom_header = {
#     'referer' : "http://www.naver.com"
#     'users-agent' = "Mozilla/5.0 (Linux; {Android Version}; {Build Tag etc.}) AppleWebKit/{WebKit Rev} (KHTML, like Gecko)Chrome/{Chrome Rev} Mobile Safari/{WebKit Rev}"
# }

# for num in range(850,857) :
#     url "https://search.daum.net/search?w=tot&DA=LOT&rtmaxcoll=LOT&&q="+str(num)
#     req = requests.get(rul)

#     if req.status_code == reqeusts.codes.ok :
#         html = BeautifulSoup(req.text, "html.parser")
#         numbers = html.select("div.lottonum.img_lotto")
#         for numbers in numbers[:6] :
#             print(number.text, end = " ")
