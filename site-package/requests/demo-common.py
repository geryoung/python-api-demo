#!/usr/bin/python# -*- coding utf-8 -*-

import requests;

r = requests.get("http://itchz.cmbchina.cn/login.htm");

print(r.text);

