import scrapy

class BasicQuestionsSpider(scrapy.Spider):
    name = 'sailing qustions base'
    start_urls = [
        'https://www.elwis.de/DE/Sportschifffahrt/Sportbootfuehrerscheine/Fragenkatalog-See/Basisfragen/Basisfragen-node.html;jsessionid=43D75A92859BCA5E67C61611A0F8ACB5.server2t2',
    ]

    def parse(self, response):
        for quest in response.xpath('//div[@id="content"]/ol[@type="1"]/li'):
            quest_dict =  {
                'question': quest.xpath('text()').get(),
                'image': quest.xpath('p/span/img/@src').get(),
                'answers': {
                    'a': quest.xpath('ol[@type="a"]/li[1]/text()').get(),  # a is always the correct answer
                    'b': quest.xpath('ol[@type="a"]/li[2]/text()').get(),
                    'c': quest.xpath('ol[@type="a"]/li[3]/text()').get(),
                    'd': quest.xpath('ol[@type="a"]/li[4]/text()').get(),
                },
                'correct_answer': 'a'
            }
            yield quest_dict


# class SpecialQuestionsSpider(scrapy.Spider):
#     name = 'sailing qustions base'
#     start_urls = [
#         'https://www.elwis.de/DE/Sportschifffahrt/Sportbootfuehrerscheine/Fragenkatalog-See/Spezifische-Fragen-See/Spezifische-Fragen-See-node.html'    
#     ]

#     def parse(self, response):
#         for quest in response.xpath('//div[@id="content"]'):
#             quest_dict =  {
#                 'question': quest.xpath('p/text()').get(),
#                 'image': quest.xpath('p/span/img/@src').get(),
#                 'answers-a': quest.xpath('ol[@type="a"]/li[1]/text()').get(),
#                 'answers-b': quest.xpath('ol[@type="a"]/li[2]/text()').get(),
#                 'answers-c': quest.xpath('ol[@type="a"]/li[3]/text()').get(),
#                 'answers-d': quest.xpath('ol[@type="a"]/li[4]/text()').get(),
#             }
#             yield quest_dict