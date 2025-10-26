import requests
from bs4 import BeautifulSoup
from FakeAgent import Fake_Agent
class Logic:
    instance : str = ""
    headers = {
        "User-Agent": f'{Fake_Agent().random()}'
    }
    def __init__(self, instance:str) -> None:
        self.instance = instance
    def sorting(self, array : list) -> list:
        temp = []
        temp_num = 1
        for i in array:
            if temp_num == 0:
                temp.append(i)
                temp_num = 1
            else:
                temp_num = 0
    
        return temp
    def checking(self, array:list) -> list:
        temp = []
        for item  in array:
            if item != "":
                temp.append(item)
    def query(self,query:str,page:int) -> list:
        query = query.replace(" ", "+")
        source = requests.get(f"{self.instance}/search?q={query}&page={page}", headers=self.headers)
        soup = BeautifulSoup(source.text, "html.parser")
        items = soup.find_all('a')
        match = ["/watch?v=", "/channel/"]
        #channel_urls = []
        #channel_names = []
        names = []
        urls = []
        for item in items:
            if (item.attrs["href"].startswith(match[0]) and not item.attrs["href"].endswith("listen=1")):
                names.append(item.contents[0].get_text().replace("\n", ""))
                urls.append("https://www.youtube.com"+item.attrs["href"])
            #if item.attrs["href"].startswith(match[1]):
            #    channel_names.append(item.contents[1].get_text().replace("\n", "").replace(" ", "").replace("\xa0", ""))
             #   channel_urls.append("https://www.youtube.com"+item.attrs["href"])
        
        return [self.sorting(urls),self.sorting(names)] #,channel_urls,channel_names
    

