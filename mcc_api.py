import json
from os.path import isfile
from requests import Session
import zlib


class Pegasus:

    def __init__(self, conf_file):
        if not conf_file or not isfile(conf_file):
            raise Exception('File %s not found.' % conf_file)
        with open(conf_file, 'rb') as f:
            self.conf = json.loads(zlib.decompress(f.read(1024)))
        f.close()
        self.session = Session()
        self.login()

    def login(self):
        url = '%s/login/%s' % (self.conf['url'], self.conf['uuid'])
        r = self.session.get(url)
        if not r.text.startswith('OK'):
            raise Exception(r.text)

    def submit(self, problem_id, input, output):
        url = '%s/submit/%s/%s/%s/%s' % (
            self.conf['url'], self.conf['uuid'], problem_id, input, output
        )
        r = self.session.get(url)
        return r.text
