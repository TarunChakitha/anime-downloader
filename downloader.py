import os
import re
import sys
import requests
import urllib.request
import subprocess as sp
from colored import fg, attr
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

reset = attr('reset')

supported_urls = [
    "https://gogoanime2.org/"
]

def welcomeBanner():
    sp.call('cls', shell=True)
    sp.call('clear', shell=True)
    print(f"""{fg("green_1")}
===============================================================================================================
||                                                                                                           ||
||     _            _                    ____                           _                    _               ||
||    / \    _ __  (_) _ __ ___    ___  |  _ \   ___  __      __ _ __  | |  ___    __ _   __| |  ___  _ __   ||
||   / _ \  | '_ \ | || '_ ` _ \  / _ \ | | | | / _ \ \ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|  ||
||  / ___ \ | | | || || | | | | ||  __/ | |_| || (_) | \ V  V / | | | || || (_) || (_| || (_| ||  __/| |     ||
|| /_/   \_\|_| |_||_||_| |_| |_| \___| |____/  \___/   \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|     ||
||                                                                                                           ||
||              Description: This tool will help you download all episodes of any anime from                 ||
||                                             www1.gogoanime.ai                                             ||
==============================================================================================================={reset}"""
    )
    print(f"""{fg('gold_1')}===============================================================================================================
||                             Programmer: Tarun Chakitha | github.com/TarunChakitha                         ||
===============================================================================================================                                    
    {reset}""")

class TqdmUpTo(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def greenLine():
    print(f"{fg('green_1')}---------------------------------------------------------------------------------------------------------------{reset}")

def whiteLine():
    print("---------------------------------------------------------------------------------------------------------------")

def redLine():
    print(f"{fg('red')}---------------------------------------------------------------------------------------------------------------")

def goldLine():
    print(f"{fg('gold_1')}---------------------------------------------------------------------------------------------------------------")

def setGreenn():
    print(f"{fg('green_1')}")

def try_another_site():
    print(f"{fg('red')}[*] [INFO] Site not working or Cloudflare is blocking the site!{reset}")
    redLine()
    print(f"{fg('sky_blue_1')}[-] [INFO] Please try using other Gogoanime sites.{reset}")

    for url in supported_urls:
        print(f"{fg('sky_blue_1')}    Alternate: {url}{reset}")

    print("Bye...")
    sys.exit()

def check_size(download_url,download_location):
    local_size = os.stat(download_location).st_size
    server_size = int(urllib.request.urlopen(download_url).info()['Content-Length'])
    if(local_size == server_size): return True
    else: return False

def downloadVideoToLocal(download_url, file_name, download_location):
    if(os.path.isfile(download_location)):
        if(check_size(download_url,download_location) == True):
            print(f"[*] [INFO] {file_name} already downloaded.")
            return
        else:
            print(f"[*] [INFO] {file_name} incomplete Download. Downloading again.")
            pass
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
    urllib.request.install_opener(opener)

    with TqdmUpTo(unit='B', unit_scale=True, unit_divisor=1024, miniters=1,
                  desc=file_name) as t:
        urllib.request.urlretrieve(
            download_url, filename=download_location, reporthook=t.update_to, data=None)
        t.total = t.n

def fetch_download_links(base_url,total_episodes):
    print(f"{fg('sky_blue_1')}[*] [INFO] Fetching download links...{reset}")
    storage_urls = []
    unsucc_eps = []
    count = 0

    for ep_num in range(1,total_episodes+1):
        url = base_url + str(ep_num)
        response = requests.get(url,stream=True)
        soup = BeautifulSoup(response.text, 'html.parser')
        if response.status_code == 200:
            for link in soup.find_all('a'):
                l = link.get('href')
                if type(l) == str and l.startswith("https://streamani.net/download"):
                    streamani_url = link.get('href')
                    break
        else:
            try_another_site()
        if streamani_url == '': 
            greenLine()
            print(f"{fg('sky_blue_1')}[-] [INFO] Found only {count} Episode(s) in total.{reset}")
            return count,storage_urls,unsucc_eps

        streamani_response = requests.get(streamani_url,stream=True)
        if(streamani_response.status_code == 200):
            episode_soup = BeautifulSoup(streamani_response.text,'html.parser')
            links = episode_soup.find_all('a')
            for index,link in enumerate(links):
                l = link.get('href')
                if l.startswith("https://storage.googleapis.com"):
                    greenLine()
                    print(f"{fg('green_1')}[*] [INFO] Found Episode Number {ep_num}")
                    storage_urls.append(l)
                    count += 1
                    streamani_url = ""
                    l = ""
                    break
                elif(index == len(links)-1):
                    unsucc_eps.append(ep_num)
                    greenLine()
                    print(f"{fg('red_1')}[*] [INFO] Episode Number {ep_num} Not Found - Skipping")
    greenLine()
    print(f"{fg('sky_blue_1')}[-] [INFO] Found {count} Episode(s) in total.{reset}")
    return count, storage_urls, unsucc_eps

def Bye():
    print(f"{fg('gold_1')}Thank you for using this scipt.")
    print("Follow me on LinkedIn @ www.linkedin.com/in/TarunChakitha")
    print(f"Bye...{reset}")
    sys.exit()

if __name__ == "__main__":
    welcomeBanner()
    try:
        Folder_name =  input(f"{fg('sky_blue_1')}Enter Anime name with season number: ")  # 'My Hero Academia Season 4'
        base = input("Paste the episode link from www1.gogoanime.ai: ") # https://www1.gogoanime.ai/boku-no-hero-academia-4th-season-episode-1
        total_episodes = input("How many episodes you want to download (default 25 - leave blank): ")
        if(total_episodes == ''): total_episodes = 25
        else: total_episodes = int(total_episodes)
        print()

        digs = re.findall(r'\d+',base)[-1]
        base_url = base[:-len(digs)]

        if(os.path.exists(Folder_name) == False): os.mkdir(Folder_name)

        count, storage_urls, unsucc_eps = fetch_download_links(base_url,total_episodes)

        print(f"\n{fg('sky_blue_1')}DOWNLOADING EPISODES...")
        print(f"{fg('white')}",end='')

        for i,url in enumerate(storage_urls,start=1):
            if(i in unsucc_eps): continue
            whiteLine()
            downloadVideoToLocal(url, Folder_name + " EP " + str(i), Folder_name + '/' + Folder_name + " EP " + str(i))
        
        whiteLine()
        print(f"{fg('sky_blue_1')}[-] [INFO] Done! {count} Episode(s) downloaded.")
        if(len(unsucc_eps) != 0):
            print()
            print(f"{fg('red_1')}[*] Sorry. The following episodes could not be downloaded.")
            for ep in unsucc_eps:
                print('--> '+Folder_name + " EP " + str(ep))
            print("As of now there is a workaround to get the missing episodes: Try downloading manually from a browser or wait till the api is up. I will fix this issue later.")
        print()
        Bye()
    except KeyboardInterrupt:
        print(f"{fg('white')}\n\nOperation Interrupted by user.\n")
        Bye()

