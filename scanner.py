#!/usr/bin/env python

import difflib
import hashlib
import requests

bags_urls = [
    'http://www.mansurgavriel.com/collections/all',

    ]

def get_content():
    #r = requests.get("http://www.mansurgavriel.com/collections/all")
    r = requests.get("http://new.yancao.me")
    return r.content

def hash_obj(content):
    hash_obj = hashlib.md5(content)
    return hash_obj.hexdigest()

def diff(old, new):
    """
    Helper function. Returns a string containing the unified diff of two multiline strings.
    """
    old=old.splitlines(1)
    new=new.splitlines(1)

    diff=difflib.unified_diff(old, new)

    return ''.join(diff)

# c1 = get_content()
# print hash_obj(c1)
# from time import sleep
# sleep(10)

# c2 = get_content()
# print hash_obj(c2)

# print diff(c1, c2)

# print hash_obj(c1) == hash_obj(c2)

r = requests.get("http://new.yancao.me")


