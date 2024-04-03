# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import re


def list_split(items, n):
    return [items[i : i + n] for i in range(0, len(items), n)]


def getdata(name):
    data = requests.get(
        f'https://github.com/users/{name.replace("=","")}/contributions'
    ).text
    datadatereg = re.compile(r'data-date="(.*?)"')
    datacountreg = re.compile(r">(.*?) contributions? on .*?</tool-tip>")
    datadate = datadatereg.findall(data)
    datacount = datacountreg.findall(data)
    datacount = list(map(int, [0 if i == "No" else i for i in datacount]))

    sorted_data = sorted(zip(datadate, datacount))
    if len(sorted_data) > 0:
        datadate, datacount = zip(*sorted_data)

    contributions = sum(datacount)
    datalist = []
    for index, item in enumerate(datadate):
        itemlist = {"date": item, "count": datacount[index]}
        datalist.append(itemlist)
    datalistsplit = list_split(datalist, 7)
    returndata = {"total": contributions, "contributions": datalistsplit}
    return returndata


def get_allow_origins():
    allow_origins = []
    try:
        file = open(os.path.join(os.getcwd(), "allow_origins.txt"))
        allow_origins = [line.strip() for line in file.readlines()]
        file.close()
    except IOError as e:
        print(e)
    finally:
        return allow_origins


def wildcard2regex(str):
    return str.replace(".", "\.").replace("*", ".*").replace("?", ".")


def get_domain(str):
    return str.replace("http://", "").replace("https://", "").split(":")[0]


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        origin = ""
        origin_domain = ""
        allow_origins = get_allow_origins()
        allowed = False
        for header, value in self.headers.items():
            if header.lower() == "origin":
                origin = value
        origin_domain = get_domain(origin)
        print(f"Request-Origin:{origin}")
        print(f"Allow-Origin:{allow_origins}")
        if origin_domain == "" or len(allow_origins) <= 0:
            allowed = True
        else:
            for allow_origin in allow_origins:
                if re.search(wildcard2regex(allow_origin), origin_domain):
                    allowed = True
                    break
        if allowed:
            user = path.split("?")[1]
            data = getdata(user)
            self.send_response(200)
            self.send_header(
                "Access-Control-Allow-Origin", "*" if origin == "" else origin
            )
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_response(400)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()


def start_server(port):
    http_server = HTTPServer(("0.0.0.0", int(port)), handler)
    http_server.serve_forever()
