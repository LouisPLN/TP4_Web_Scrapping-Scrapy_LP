import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsBoursoramaItem
import time

class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://www.boursorama.com/bourse/actions/palmares/france/?page={n}' for n in range(1,10)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)
            
    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[1:]
        
        for indices in liste_indices:
            item = ReviewsBoursoramaItem()
            
            #indice boursier
            try: 
              item['indice'] = indices.css('a.c-link c-link--animated::text').extract()[0].strip()
            except:
              item['indice'] = 'None'
            
            #indice cours de l'action
            try:
              item['cours'] 
            except:item['cours'] = 'None'
            
            #Variation de l'action
            try: 
              item['var'] 
            except:
              item['var'] = 'None'
            
            #Valeur la plus haute
            try: 
              item['hight'] 
            except:
              item['hight'] = 'None'
            
            #Valeur la plus basse
            try: 
              item['low']
            except:
              item['low'] = 'None'

            #Valeur d'ouverture
            try: 
              item['open_']
            except:
              item['open_'] = 'None'

            #Date de la collecte
            try: 
              item['time'] 
            except:
              item['time'] = 'None'

            
            yield item