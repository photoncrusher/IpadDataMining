import scrapy

class IpadItem(scrapy.Item):
    name = scrapy.Field()
    screen = scrapy.Field()
    resolution = scrapy.Field()
    panel = scrapy.Field()
    CPU = scrapy.Field()
    ROM = scrapy.Field()
    RAM = scrapy.Field()
    rear_cam = scrapy.Field()
    front_cam = scrapy.Field()
    SIM = scrapy.Field()
    security = scrapy.Field()
    weigth = scrapy.Field()
    operatingsys = scrapy.Field()
    warranty = scrapy.Field()
    status = scrapy.Field()
    available = scrapy.Field()

    pass