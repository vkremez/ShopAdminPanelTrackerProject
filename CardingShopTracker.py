#!/usr/bin/env python
# Coded by Vitali
import urllib
import sqlite3
import re

u = urllib.urlopen('http://www.cybercrime-tracker.net/index.php?s=0&m=40&search=Carder%20shop')

data = u.read().split('/>')

rdate = re.findall(r'<tr><td>([0-9-]{10})</td>', str(data))

url = re.findall(r'latest-scan/http://(.{8,40})/', str(data))

ip = re.findall(r'/ip-address/([0-9\.]{0,20})/information/', str(data))

rtype = []
for i in range(len(ip)):
	i = 'CardingShopAdminPanel'
	rtype.append(i) 

rsource = []
for i in range(len(url)):
	i = 'CyberCrimeTracker.net'
	rsource.append(i)
zipped = zip(rdate, url, ip, rtype, rsource)

f = open('ips.txt', 'w+')
for i in ip:
	f.write(i+'\n')
f.close()

conn = sqlite3.connect('CardingShopAdminPanel.sqlite')
cur = conn.cursor()
conn.text_factory = str
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS CardingShopAdminPanel;
CREATE TABLE CardingShopAdminPanel (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    rdate 	TEXT,
    url     TEXT,
    ip		TEXT,
    rtype	TEXT,
    rsource TEXT
);
''')

for element in zipped:
	rdate = element[0]
	url = element[1]
	ip = element[2]
	rtype = element[3]
	rsource = element[4]

	cur.execute('''INSERT OR IGNORE INTO CardingShopAdminPanel (rdate, url, ip, rtype, rsource) VALUES ( ?, ?, ?, ?, ? )''', ( rdate, url, ip, rtype, rsource ) )
    #cur.execute('SELECT id FROM Hosts WHERE name = ? ', ( name, ))

conn.commit()