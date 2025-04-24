import threading
import requests

'''
https://python.langchain.com/docs/introduction/
https://python.langchain.com/docs/concepts/
https://python.langchain.com/docs/tutorials/
'''

from bs4 import BeautifulSoup

url=[
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/tutorials/'
]

def fetch_context(url):
    responce=requests.get(url)
    soup=BeautifulSoup(responce.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]

for i in url:
    thread=threading.Thread(target=fetch_context,args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All threads are done')