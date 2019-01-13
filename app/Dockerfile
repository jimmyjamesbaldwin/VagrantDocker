FROM library/alpine:latest

RUN apk update

RUN apk add nginx

COPY nginx.conf /etc/nginx/nginx.conf

COPY index.html /tmp/index.html

COPY certs/dhparam.pem /etc/ssl/certs/dhparam.pem

COPY certs/self-signed.conf /etc/nginx/snippets/self-signed.conf

COPY certs/ssl-params.conf /etc/nginx/snippets/ssl-params.conf

COPY certs/nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt

COPY certs/nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key

RUN mkdir -p /run/nginx # this directory is required by nginx

EXPOSE 80

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]