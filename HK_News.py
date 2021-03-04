import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.politifact.com/factchecks/list/?page='+str(page)#Use the browser to get the URL. This is a suspicious command that might blow up.page = requests.get(url)