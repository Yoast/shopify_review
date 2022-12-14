import scrapy
from shopify_review.items import ShopifyReviewItem



class ReviewSpider(scrapy.Spider):
    name = 'review'
    allowed_domains = ['shopify.com']
    start_urls =  ['https://apps.shopify.com/yoast-seo/reviews']

    def parse(self, response):
        general_score = response.xpath('/html[1]/body[1]/main[1]/section[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]').get()
        general_score = general_score.replace('<div aria-label=\"4.5 out of 5 stars\">\n      ','')
        general_score = general_score.replace('\n    </div>','')
        item = ShopifyReviewItem()
        item['general_score'] = general_score
        yield item
        


