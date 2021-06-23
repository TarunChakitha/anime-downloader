import os
import re
import sys
import random
import requests
import youtube_dl
import youtube_dl.utils
import subprocess as sp
from colored import fg, attr
from bs4 import BeautifulSoup

reset = attr('reset')

supported_urls = [
    "https://gogoanime2.org/"
]

User_agents = [
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/74.0.3729.157 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7"
"Mozilla/5.0 (Linux; Android 5.1.1; KFSUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/80.5.3 like Chrome/80.0.3987.162 Safari/537.36"
"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; Kindle Fire Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
"Mozilla/5.0 (Linux; Android 5.1.1; KFSUWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/78.4.6 like Chrome/78.0.3904.108 Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/80.5.3 like Chrome/80.0.3987.162 Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1.1; KFFOWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/76.3.6 like Chrome/76.0.3809.132 Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1.1; KFGIWI) AppleWebKit/537.36 (KHTML, like Gecko) Silk/80.5.3 like Chrome/80.0.3987.162 Safari/537.36"
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
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

def Bye():
    print(f"{fg('gold_1')}Thank you for using this scipt.")
    print("Follow me on LinkedIn @ www.linkedin.com/in/TarunChakitha")
    print(f"Bye...{reset}")
    sys.exit()

def greenLine():
    """
    Prints a green line
    """
    print(f"{fg('green_1')}---------------------------------------------------------------------------------------------------------------")

def whiteLine():
    """
    Prints a white line
    """
    print("---------------------------------------------------------------------------------------------------------------")

def redLine():
    """
    Prints a red line
    """
    print(f"{fg('red')}---------------------------------------------------------------------------------------------------------------")

def goldLine():
    """
    Prints a gold line
    """
    print(f"{fg('gold_1')}---------------------------------------------------------------------------------------------------------------")

def setGreenn():
    """
    Sets the terminal font color to green
    """
    print(f"{fg('green_1')}",end='')

def try_another_site():
    print(f"{fg('red')}[*] [INFO] Site not working or Cloudflare is blocking the site!{reset}")
    redLine()
    print(f"{fg('sky_blue_1')}[-] [INFO] Please try using other Gogoanime sites.{reset}")

    for url in supported_urls:
        print(f"{fg('sky_blue_1')}    Alternate: {url}{reset}")

    print("Bye...")
    sys.exit()

def my_hook(d):
    """
    A reporthook for youtube-dl
    """
    if d['status'] == 'downloading':
        if(d['speed'] != None):
            speed = round(d['speed']/1e+6,3) if d['speed'] else '-'
            print(f" [*] [STATUS] Downloading - {round(float(d['downloaded_bytes'])/float(d['total_bytes'])*100,3)} % Speed - {speed} MBps ETA - {d['_eta_str']} min   ",end='\r')

def downloadVideoToLocal(download_url, file_name, download_location):
    """
    Downlaods the video from storage.googleapi url to yuor local machine.
    Note--> Incase the download is interrupted, re-run the script and it will resume downloading from the last downloaded byte.
    """
    youtube_dl.utils.std_headers['User-Agent'] = random.choice(User_agents)
    ydl_opts = {'format': 'best',
    'quiet': True,
    'no_warnings': True,
    'ignoreerros': True,
    'outtmpl': download_location,
    'progress_hooks': [my_hook]
    }

    setGreenn()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(file_name)
        ydl.download([download_url])
    print(f"[-] [STATUS] Download finished.                                             ")
    
def fetch_download_links(base_url,total_episodes):
    """
    Fetches the storage.googleapis.com video source url from the episode url
    Note--> Sometimes the googleapis link does not appear and the video plays from a blob url. 
    It cannot fetch the url if it's a blob url so some episodes may not be downloaded.
    """
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
                    storage_urls.append((ep_num,l))
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

if __name__ == "__main__":
    welcomeBanner()
    try:
        Folder_name =  input(f"{fg('sky_blue_1')}Enter Anime name along with season number: ")  # My Hero Academia Season 4
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

        for tup in storage_urls:
            greenLine()
            file_name = Folder_name + " EP "
            downloadVideoToLocal(tup[1], file_name + str(tup[0]), f"{Folder_name}/{file_name}{tup[0]}")

        greenLine()

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
        print("\r"+" "*100)
        print(f"{fg('white')}\nOperation Interrupted by user.\n")
        Bye()


