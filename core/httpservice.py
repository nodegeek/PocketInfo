import requests as request

__author__ = 'Santhosh'



class HttpRequest:
    def __init__(self):

        self.request_headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language' :	'en-US,en;q=0.5',
                'Connection' : 'keep-alive',
        }


    def get_response(self, URL, headers = None):
        if not headers:
            headers = self.request_headers
        response = request.get(URL, headers = headers, allow_redirects = True)
        print response.status_code

        return response


