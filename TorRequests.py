import os
os.chdir(r"C:\Users\ratin\Desktop\Tor Browser\Browser")


import csv
import http.client

# library for Tor connection
import socket
import subprocess
import time
import urllib

import requests
import socks
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

class Trequests:
        def __init___(self):
                self.something = "nothing"
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
                socket.socket = socks.socksocket
                print("Connected to Tor")

        def launchTor(self):
                # start Tor (wait 30 sec for Tor to load)
                sproc = subprocess.Popen(r'./firefox.exe')
                # time.sleep(30)
                return sproc

        def killTor(self, sproc):
                sproc.kill()

        def set_new_ip(self):
                # disable socks server and enabling again
                socks.setdefaultproxy()
                """Change IP using TOR"""
                with Controller.from_port(port=9151) as controller:
                        controller.authenticate()
                        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
                        socket.socket = socks.socksocket
                        controller.signal(Signal.NEWNYM)

        def checkIP(self):
                conn = http.client.HTTPConnection("icanhazip.com")
                conn.request("GET", "/")
                time.sleep(3)
                response = conn.getresponse()
                print('current ip address :', response.read())

        def get(self,url,headers):
                self.set_new_ip()
                return requests.get(url,headers)
