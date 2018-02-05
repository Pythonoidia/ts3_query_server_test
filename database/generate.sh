#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
for f in "$DIR"/*.sql
do
    echo Creating db from "$f"
    cat "$f" | sqlite3 ts3server.sqlitedb
done
