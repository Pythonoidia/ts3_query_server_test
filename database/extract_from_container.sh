#!/bin/bash

docker cp ts3queryservertest_ts3_1:/app/ts3server.sqlitedb ts3server_temp.sqlitedb
docker cp ts3queryservertest_ts3_1:/app/ts3server.sqlitedb-wal ts3server_temp.sqlitedb-wal
docker cp ts3queryservertest_ts3_1:/app/ts3server.sqlitedb-shm ts3server_temp.sqlitedb-shm
sqlite3 ts3server_temp.sqlitedb .dump > database/ts3server.sql
rm ts3server_temp.sqlitedb*
