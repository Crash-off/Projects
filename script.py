import requests
RESET = "\033[0m"
def print_banner(style="hacker", version=None, author=None):
    v = f" v{version}" if version else ""
    a = f" • {author}" if author else ""
    if style == "professional":
        BLUE = "\033[1;34m"
        print(BLUE + "SUBSCAN && DIRSCAN" + RESET)
        if version or author:
            print(BLUE + f"{'Version:':<8} {version or '-'}    {'Author:':<8} {author or '-'}" + RESET)
        print("-" * 40 + "\n")


wordlist = ["admin", "site", "help", "support", "mail", "loja", "painel"]

def subdir(site):
    for words in wordlist:
        try:
            form = f"https://{words}.{site}/"
            r = requests.get(form)
            a = r.status_code
            if a == 200:
                print("SITE 200:", form)
            elif a == 301:
                print(f"MOVIDO PERM 301: {form}")
        except:
            pass

dirlist = ["index.html", "robots.txt", "painel", "seek", "wordpress", "0", "login", "acess", "admin", "register"]

def dirscan(sitef):
    for dir in dirlist:
        try:
            fmat = f"https://{sitef}/{dir}/"
            f = requests.get(fmat)
            g = f.status_code
            if g == 200:
                print(f"DIRETORIO 200: {fmat}")
            if g == 301:
                print(f"DIRETORIO 301: {fmat}")
        except:
            pass

if __name__ == '__main__':
    print_banner("professional", version="0.1", author="Crash")
    url = input("Qual o site?:\n")
    op = input("Select a Option:\n 1 - SUBSCAN\n 2 - DIRSCAN\nDigit:")
    if op == "1":
        subdir(url)
    elif op == "2":
        dirscan(url)
