# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    ranking = scrapy.Field()  # 排名
    mid = scrapy.Field()  # ID
    name = scrapy.Field()  # 电影名
    english_name = scrapy.Field()  # 英文名
    release_year = scrapy.Field()  # 上映年限
    default_image = scrapy.Field()  # 图片
    box_office = scrapy.Field()  # 票房
    area = scrapy.Field()  # 地区
    area_id = scrapy.Field()  # 地区ID
    week = scrapy.Field()  # 周数
    week_time = scrapy.Field()  # 每周时间
    average_per_game = scrapy.Field()  # 平均每场人次
    one_week_box_office = scrapy.Field()  # 周票房
    total_box_office = scrapy.Field()  # 总票房
    days_released = scrapy.Field()  # 上映天数
    director = scrapy.Field()  # 导演
    starring = scrapy.Field()  # 明星
    production_company = scrapy.Field()  # 制作公司
    publish_company = scrapy.Field()  # 出版公司
    movie_type = scrapy.Field()  # 电影类型
    duration = scrapy.Field()  # 片长
    release_time = scrapy.Field()  # 上映时间
    style = scrapy.Field()  # 制式
