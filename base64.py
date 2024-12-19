import argparse
import base64


def encode64(string):
    string = string.encode("utf-8")
    string = base64.b64encode(string)
    return string.decode('utf-8')


def decode64(string):
    try:
        string = base64.b64decode(string)
        string = string.decode('utf-8')
        return string
    except Exception as e:
        return "提供内容解密失败"


if __name__ == '__main__':
    banner = """

    ░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓████████▓▒░░▒▓██████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░       ░▒▓█▓▒░ 

    """
    print(banner)
    # 实体化对象
    parser = argparse.ArgumentParser(description="这个是一个thinkphp RCE监测脚本")
    parser.add_argument("-e", "--encode", help="编码", dest="b64estring")
    parser.add_argument("-d", "--decode", help="解码", dest="b64dstring")
    # 调用对象的parse_args方法
    args = parser.parse_args()
    b64estring = args.b64estring
    b64dstring = args.b64dstring
    if b64estring:
        result = encode64(b64estring)
        print(f'编码过后的内容：{result}')
    elif (b64dstring):
        result = decode64(b64dstring)
        print(f'解码过后的内容：{result}')
    else:
        print("请提供编码或解码选项。使用 -h 获取帮助信息。")




