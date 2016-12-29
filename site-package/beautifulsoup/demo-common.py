#!/usr/bin/python# -*- coding utf-8 -*-


from BeautifulSoup import BeautifulSoup


html_doc="""<!DOCTYPE html>
<html>
<head>
  <title>aaa</title>
</head>
<body>
<div id=""></div>
</body>
</html>"""


soup = BeautifulSoup(html_doc);
print(soup.title);