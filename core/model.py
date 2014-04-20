from core.database import get_db_connection

__author__ = 'Santhosh'

class Model:
    def __init__(self, db):
        pass


    def save(self):
        model = self.__dict__
        self.db.news.insert(model)


class ExtractorStats(Model):
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.created_date = None
        self.last_updated = None
        self.exit_status = None
        self.feeds_extracted = 0
        self.feeds_found = 0
        self.is_invalid_feed = 0

    def validate_model(self):
        print ''

class News(Model):
    def __init__(self):
        #self.id = ObjectId()
        self.publish_date = None
        self.title = None
        self.description = None
        self.full_article = None
        self.image_url = None
        self.is_valid = True

