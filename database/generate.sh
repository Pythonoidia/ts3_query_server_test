#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cat "$DIR"/ts3server.sql | sqlite3 ts3server.sqlitedb
