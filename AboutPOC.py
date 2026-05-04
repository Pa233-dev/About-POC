import requests
import csv
import warnings
import urllib3
import time
import socket
import signal
class RequestTimeout(Exception):
    pass
def handler(signum,frame):
    raise RequestTimeout("超时")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
socket.setdefaulttimeout(10)
urls = []
ppost = []
webs = open("net.csv",'r',encoding='utf-8')
reader = csv.reader(webs,quotechar='"')
for num,row in enumerate(reader,1):
    if row:
        urls.append(row[-1].strip())
        ppost.append(row[2].strip())
body = """填入包体"""
for i in range(len(urls)):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(12)
    try:
        target = urls[i]+"填入url后缀"
        head = {
        "可": ppost[i],
        "替": "",
        "换": "",
        "为": "",
        "包": "",
        "头": "",
        }
        response = requests.post(
            url = target,
            headers = head,
            data = body.encode('utf-8'),
            timeout = (5,4),
            verify=False
            )
        signal.alarm(0)
        if "填入预期内容" in response.text:
            print(urls[i])
    except RequestTimeout:
        continue
    except Exception:
        continue
    finally:
        signal.alarm(0)
webs.close()
