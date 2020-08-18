import scrapy
import pandas as pd
from zendeskchat.items import ZendeskchatItem


class ZendeskChatSpider(scrapy.Spider):
    sites_path = '/home/luisca1985/Documentos/Freelancer/17082020-web scraping/zendesk-chat-project/zendeskchat/static/sites.csv'
    sites = pd.read_csv(r""+sites_path,encoding='utf8')
    count = 5
    name = 'zendesk_chat'
    #allowed_domains = sites['Domain'][:count].tolist()
    #start_urls = res = ['http://' + url for url in sites['Location on Site'][:count].tolist()]
    allowed_domains = ['barklypets.com/']
    start_urls = ['https://barklypets.com/']

    def parse(self, response):
        item = ZendeskchatItem()
        pattern = r'(?:\$zopim | zE\(\'webWidget)'
        script = response.xpath('//head/script').re_first(pattern)
        item["url"] = response.url
        item["response"] = script
        yield item