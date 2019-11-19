import requests
import re

from typing import List, Union

from timer import Timer, TimerResponse

class AioUrlCollector(Timer):
    # AioUrlCollect(1, 2, hello='world')
    def __init__(self, *args, **kwargs):
        # *args = [1, 2], **kwargs = {"hello": "world"}
        super().__init__(*args, **kwargs)
        # super().__init__(1, 2, hello='world')
    
    def getUrls(self, url: str) -> list:
        try:
            resp = requests.get(url)
        except requests.exceptions.ConnectionError:
            return []
        
        if resp.status_code == 200:
            found_urls = re.findall('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', resp.text)
            unique_urls = set([broken_url[0]+'://'+broken_url[1] for broken_url in found_urls])
            return list(unique_urls)
        
        return []
    
    def collect_and_time(self, urls: Union[str, List[str]]) -> TimerResponse:
        if type(urls) == str:
            urls = [urls]
        
        return self.run(self.collect, urls)

    def collect(self, urls: Union[str, List[str]]) -> list:
        if type(urls) == str:
            urls = [urls]
        
        collected = [u for url in urls for u in self.getUrls(url)]
        return collected
    

def test():
    collector = AioUrlCollector()
    cot = collector.collect_and_time('https://www.github.com')
    results = cot.results
    cot2 = collector.collect_and_time(results)
    print(cot2.elapsed, len(cot2.results))
            
if __name__ == '__main__':
    test()
