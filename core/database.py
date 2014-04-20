from pymongo import Connection
from pymongo.errors import ConnectionFailure
import sys
import appconfig
import pymongo

__author__ = 'Santhosh'


def get_db_connection():
    try:
        app_config_dict = appconfig.get_config(appconfig.DATA_BASE_CONFIG)
        host = app_config_dict['host']
        port = app_config_dict['port']
        db_name = app_config_dict['name']
        client = pymongo.MongoClient(host, int(port))
        db = client[db_name]
    except ConnectionFailure, e:
        raise ConnectionFailure

    cursor = db.news.find()
    for user  in db.news.find():
        #print user
        pass

    return db



