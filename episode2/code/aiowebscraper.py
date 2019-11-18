import requests
import asyncio
import re

from typing import Union, List
from concurrent.futures import ThreadPoolExecutor

from timer import Timer, TimerResponse

class AioUrlCollector(Timer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def getUrls(self, url: str) -> list:
        try:
            resp = requests.get(url)
        except requests.exceptions.ConnectionError:
            # failed to establish connection 
            return []
        except requests.exceptions.MissingSchema as err:
            return []
        if resp.status_code == 200:
            found_urls = re.findall('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', resp.text)
            unique_urls = set([url[0]+'://'+url[1] for url in found_urls])
            return list(unique_urls)
        return []

    def collect_and_time(self, urls: Union[str, List[str]]) -> TimerResponse:
        if type(urls) == str:
            urls = [urls]
        # get first group of next urls
        return self.run(self.collect, urls)

    def collect(self, urls: Union[str, List[str]]) -> list:
        if type(urls) == str:
            urls = [urls]
        # get first group of next urls
        collected = []
        collected.extend([u for url in urls for u in self.getUrls(url)])
        return collected



def test():
    collector = AioUrlCollector()
    collected_urls = collector.collect_and_time('https://www.github.com')
    print(collected_urls.elapsed, len(collected_urls.results))

if __name__ == '__main__':
    test()