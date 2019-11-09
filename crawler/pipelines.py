# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import requests

from sqlalchemy.orm import sessionmaker
from .models import Movie, db_connect, create_table, MovieBoxOffice

from crawler.tool import sftp_upload


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class MoviePipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save deals in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()

        movie = Movie()

        movie.ranking = int(item['ranking'])
        movie.mid = int(item['mid'])
        movie.name = item['name']
        movie.english_name = item['english_name']
        movie.release_year = item['release_year']
        movie.default_image = item['default_image']
        movie.style = item['style']
        movie.release_time = item['release_time']
        movie.duration = item['duration']
        movie.movie_type = item['movie_type']
        movie.director = item['director']

        movie.starring = item['starring'] if len(item['starring']) < 512 else item['starring'][:512]

        movie.production_company = item['production_company']
        movie.publish_company = item['publish_company']

        try:
            movie.box_office = int(item['box_office'])
        except ValueError:
            print('box_office: ' + item['box_office'])
            movie.box_office = 0

        movie.area = item['area']
        movie.area_id = int(item['area_id'])

        mbolist = []
        for i in range(len(item['week'])):
            movie_box_office = MovieBoxOffice()
            movie_box_office.mid_id = movie.mid
            movie_box_office.week = item['week'][i]
            movie_box_office.week_time = item['week_time'][i]
            movie_box_office.average_per_game = item['average_per_game'][i]
            movie_box_office.one_week_box_office = item['one_week_box_office'][i]
            movie_box_office.total_box_office = item['total_box_office'][i]

            try:
                movie_box_office.days_released = item['days_released'][i]
            except Exception as e:
                movie_box_office.days_released = 0

            mbolist.append(movie_box_office)

        try:
            session.add(movie)
            session.commit()

            for mbo in mbolist:
                session.add(mbo)

            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item




