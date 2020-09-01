import json
from os.path import isfile
from requests import Session
import zlib


class Pegasus:

    def __init__(self, conf_file, test=False):
        if not conf_file or not isfile(conf_file):
            raise Exception('File %s not found.' % conf_file)
        with open(conf_file, 'rb') as f:
            self.conf = json.loads(zlib.decompress(f.read(1024)))
        f.close()
        self.session = Session()
        status = self.login(test)

    def login(self, test):
        url = '%s/login/%s' % (self.conf['url'], self.conf['uuid'])
        # url = '%s/login/%s' % ('http://127.0.0.1:8080', self.conf['uuid'])
        r = self.session.get(url)
        if not r.text.startswith('OK'):
            raise Exception(r.text)
        if test:
            print(r.text)

    def submit(self, problem_id, input, output):
        url = '%s/submit/%s/%s/%s/%s' % (
            self.conf['url'], self.conf['uuid'], problem_id, input, output
            # 'http://127.0.0.1:8080', self.conf['uuid'], problem_id, input, output
        )
        r = self.session.get(url)
        return r.text

    def attempt(self, problem_id):
        url = '%s/attempt/%s/%s' % (
            self.conf['url'], self.conf['uuid'], problem_id
            # 'http://127.0.0.1:8080', self.conf['uuid'], problem_id
        )
        r = self.session.get(url)
        return r.text
