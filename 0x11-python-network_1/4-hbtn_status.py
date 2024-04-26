#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
