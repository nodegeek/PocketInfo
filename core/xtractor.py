from PIL import Image
import appconfig
import glob, os
__author__ = 'Santhosh'

class Xtractor(object):


    def parse_url(self):
        print 'Inside parse_url'
        return

    def start(self):
        print 'INSIDE STRAT'
    def end(self):
        print 'INSIDE END'


    def create_thumbnails(self, infile):
        size = 128, 128
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(file + ".thumbnail", "JPEG")


def get_appconfig(key):
    return appconfig.get_config(key)