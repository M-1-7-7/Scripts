from pwn import *
import requests
from bs4 import BeautifulSoup

Context.log_level = 'debug'
url = 'http://x.x.x.x:xxxx/'
cookies = {'PHPSESSID': 'xxxx'}

response = request.get(url, cookies=cookies) # initial request

# Loop untill we fing the flag
while 'keyWord' not in responce.txt:
  #extract content from <h3> tag
  extracted = BeautifulSoup(response.txt, features="lxml").h3.contents[0]

  #hashed = md5sumhex(extracted.encode())
  debug('hash: %s', hashed)

  #submit the hash
  response = requests.post(url, data={'hash': hahsed}, cookies=cookies)

extracted = BeautifulSoup(response.text, features="lxml).p.contents[0]
warn(extracted)
