FROM ubuntu:latest
FROM nginx:alpine
COPY index.html ./usr/share/nginx/html

EXPOSE 80