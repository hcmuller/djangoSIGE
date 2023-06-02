FROM alpine:3.16
RUN mkdir -p /opt/djangoSIGE/
WORKDIR /opt/djangoSIGE/
COPY requirements.txt /opt/djangoSIGE/

RUN apk update
RUN apk add --no-cache libffi-dev \ 
    libressl-dev \ 
    py3-cffi  \ 
    zlib-dev  \ 
    gcc  \ 
    jpeg-dev \ 
    linux-headers  \ 
    libxml2-dev  \ 
    libxslt-dev \ 
    musl-dev  \ 
    python3-dev \ 
    python3 \ 
    py3-pip \ 
    postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
RUN pip install gunicorn psycopg2
