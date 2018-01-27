FROM debian:jessie

MAINTAINER kszychu

ENV TS_VERSION LATEST
ENV LANG C.UTF-8

WORKDIR /app
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install bzip2 wget ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q http://dl.4players.de/ts/releases/3.0.13.8/teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2 \
    && tar -j -x -f teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2 --strip-components=1 \
    && rm -f teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2

COPY data/query_ip_whitelist.txt query_ip_whitelist.txt
COPY data/ts3server.sqlitedb ts3server.sqlitedb

EXPOSE 9987/udp 10011 30033


CMD ["./ts3server_minimal_runscript.sh"]
