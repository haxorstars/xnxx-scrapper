import requests,os,sys,re,unicodedata
from bs4 import BeautifulSoup as bes 
from concurrent.futures import ThreadPoolExecutor as thd
from sys import platform

def cek_os():
  if platform == "linux" or platform == "linux2":
    os.system("clear")
  elif platform == "win32":
    os.system("cls")

def generate_id(url):
  for i in range(10):
    x = requests.get(f"https://www.xnxx.com/search/{url}/0").text
    opn = re.findall(r' /></a></div></div><div class="thumb-under"><p><a href="(.*?)"',x)
  #  print(opn)
    if len(opn) != 0:
      print(f"Page : {i}")
      with thd(max_workers=80) as th:
        with requests.Session() as r:
         for i in opn:
            th.submit(main,i,r)
def download_bkp(f):
  pp = open(f,"r").read().splitlines()
  with thd(max_workers=80) as th:
    for i in pp:
      title,link = i.split("|")
      main2(title,link)
def main2(title,url):
  r = requests.get(url,stream=True)
  with open(f"bokep/{title}.mp4", 'wb') as file:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
  print(f"{title} Done")
def main(url,r):
 try:
  scr = r.get("https://xnxx.com"+url).text
  o = re.findall(r'"name": "(.*?)"',scr)
  if len(o) != 0:
    print(f"Judul : {o[0]}")
  else:
    print(f"Judul : -")
  x = re.findall(r'contentUrl": "(.*?)",',scr)
  if len(x) != 0:
    for i in x:
      print(f"Link Download : {i}")
      open("url-download.txt","a").write(f"{o[0]}|{i}\n")
      open("url-saved.txt","a").write(f"Judul: {o[0]}\nLink Download: {i}\n")
  else:
    print(f"Link Download Tidak Tersedia")
 except Exception as e:
   print(f"Error {e}")
if __name__ == "__main__":
  cek_os()
  if len(sys.argv) == 2:
    if sys.argv[1] == "download":
      download_bkp("url-download.txt") 
    else:
      generate_id(sys.argv[1])
  else:
    print('Argument Tidak Valid\n\nContoh Argument\nSearch Bokep: python xnxx.py "Judul Video"\nDownload Bokep: python xnxx.py download')