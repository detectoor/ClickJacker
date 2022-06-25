# Tools Name	: Clickjacker
# Contributor	: professor

from urllib.request import urlopen
from sys import argv, exit
from colorama import Fore

__author__ = 'Professor'

def check(url):
    ''' check given URL is vulnerable or not '''

    try:
        if "http" not in url: url = "http://" + url

        data = urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers: return True

    except: return False

def main():
    ''' Everything comes together '''

    try: sites = open(argv[1], 'r').readlines()
    except: print("[*] Usage: python(3) file.py <file_name>"); exit(0)

    for site in sites[0:]:
        status = check(site)

        if status:
            print(Fore.RED+" [+] "+Fore.LIGHTYELLOW_EX+site.split('\n')[0]+Fore.RED+" may be vulnerable to Clickjacking!   "+Fore.WHITE+"Verification Link:"+Fore.CYAN+"http://web.clickjacker.io/test?url=http://"+site.split('\n')[0])

        elif not status: print(Fore.GREEN+" [-] " + Fore.MAGENTA+site.split('\n')[0]+Fore.GREEN+" is not vulnerable!")
        else: print(Fore.RED+'Every single thing is crashed, Python got mad, Brother... Install it again or Send me Email: bughuntar@gmail.com')

if __name__ == '__main__': main()
