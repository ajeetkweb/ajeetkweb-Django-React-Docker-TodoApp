FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

# Build psycopg2-binary from source -- add required required dependencies
# RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
#         pip install --no-cache-dir -r requirements.txt && \
#         apk --purge del .build-deps

RUN pip install --upgrade pip && \
    apk add --upgrade --no-cache postgresql-client && \
    apk add --update --no-cache --virtual  .tmp-build-dev \
        build-base postgresql-dev musl-dev && \
    pip install -r requirements.txt && \
    apk del .tmp-build-dev

COPY . /app/backend/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]