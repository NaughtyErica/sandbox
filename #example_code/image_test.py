# -*- coding: utf-8 -*-

import json
import logging
import requests


class HTTPHandlerDB(logging.Handler):

    def emit(self, record):
        log_entry = self.format(record)
        url = 'https://db-for-logging-vkbot.herokuapp.com/api/events/'
        content_request = requests.post(url=url,
                                        data=json.dumps({'msg': log_entry}),
                                        headers={"Content-type": "application/json"}).content
        return content_request


log_db = logging.getLogger('http_log')
log_db.setLevel(logging.INFO)
log_db.addHandler(HTTPHandlerDB())


def main():
    log_db.info('Тест на запись лога в заснувшее АПИ')


if __name__ == '__main__':
    main()

