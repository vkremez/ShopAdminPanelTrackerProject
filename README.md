# CardingShopAdminPanelProject

Author: Vitali Kremez

Powered by SQLite, Python, JavaScript, HTML, GoogleMap API, IP-API JSON API

Creates a SQL table with over 20 known carding shop admin panels and visualizes the database via GoogleMap API.

Usage:

(1) Run Loader.py to create monolithic "CardingShopAdminPanel.sqlite" database with columns rdate, url, ip, rtype, rsource);

(2) Run IPConverter.py to convert hostnames to cities using http://ip-api.com JSON API and post data to "where.data";

(3) Run Geoload.py to parse "where.data", obtain lat/long values using Google MAP API, and store values in another database "geodata.sqlite";

(4) Run Geodump.py to map the data from "geodata.sqlite" to Javascript file "where.js";

(5) View the Google-mapped values in "where.html" that points to "where.js".
