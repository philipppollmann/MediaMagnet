FROM ubuntu:latest
LABEL authors="philipppollmann"

ENTRYPOINT ["top", "-b"]