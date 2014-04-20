import requests as request
import re
from bs4 import BeautifulSoup as Soup
import datetime, time
from xtractor import Xtractor
from httpservice import HttpRequest
import database
import appconfig
import image
import regex
import os


URL = 'http://www.thehindu.com/news/cities/Mangalore/?service=rss'
http_request = HttpRequest()
http_response = http_request.get_response(URL, headers =appconfig.get_config(appconfig.REQ_HEADERS_MOZILLA))
soup = Soup(http_response.content)
item_list = soup.find_all('item')
#print item_list

class HinduExtractor(Xtractor):

    def parse_url(self):
        db = database.get_db_connection()
        image_path = ''
        for item in item_list:
            news ={}
            title =  item.find('title').text
            href_link = item.find('link').text
            publish_date = item.find('pubdate').text
            description  =  item.find('description').text


            match=re.search(r'(.*)\.<img', description)
            if match:
                description =  match.group(1)
            else:
                description = ''


            news['title'] = title
            #print title
            news['description'] = description
            news['link'] = href_link
            news['pubDate'] = publish_date
            news['created_date'] =  datetime.datetime.utcnow()

            req = request.get(href_link, headers = appconfig. get_config(appconfig.REQ_HEADERS_MOZILLA), allow_redirects = True)
            soup = Soup(req.content)


            tag = soup.find("div",{"id": "hcenter"})
            size = size = 256, 256
            if tag:
                image_link =  (tag.find('img'))['src']
                req = request.get(image_link)
                image_name =regex.remove_white_spaces.sub('',title[:10]+".jpg")
                path = appconfig.get_config(appconfig.IMAGE_PATH)
                path = (path['thumbnail_path']).strip()
                now = datetime.datetime.now()
                folder_name = str(now.strftime("%Y_%m_%d"))
                path = path+folder_name+"/"

                image_path = image.create_thumbnail(size, req.content, image_name, path)
                if not os.path.exists(path):
                    os.makedirs(path)
                news['thumbnail_path'] = image_path
            db.news.insert(news)



            '''
            c =0
            for atricle in db.news.find():
                print "TITLE: ",atricle['title']
                print "DESC:", atricle['description']
                print "THUMB PATH:", atricle.get('thumbnail_path')
                print "LINK: ", atricle['link']
                print "PUB DATE:", atricle['pubDate']
                print "CREATED_DATE",atricle['created_date']
                print '===================================================='
                print '\n'
                c = c+1

            print '============================================================================================\n',c
            '''



HinduExtractor().parse_url()










