import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'\x95T\xedl\x1a\xefF\xd7\xa3u+p\xfbR\xe6\xa7'