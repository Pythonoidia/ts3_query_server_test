#!/bin/bash

docker cp ts3:/app/ts3server.sqlitedb ts3server_temp.sqlitedb
sqlite3 ts3server_temp.sqlitedb .dump > database/ts3server.sql
rm ts3server_temp.sqlitedb
