import psycopg2
import os
import definition
import pytest
import json


@pytest.fixture(scope='session')
def db_config():
    path = os.path.join(definition.ING_DIR, 'models', 'db.json')
    config = json.loads(open(path).read())

    yield config


@pytest.fixture(scope='session')
def db_conn(db_config):
    conn = psycopg2.connect(**db_config)
    yield conn
    conn.close()


@pytest.fixture(scope='session')
def db_cur(db_conn):
    cur = db_conn.cursor()
    yield cur
    cur.close()
    db_conn.rollback()


@pytest.fixture(scope='session')
def data_txt():
    path = 'tests/ingestion/data/d2.txt'
    with open(path) as txt:
        data = txt.read()
    return data


@pytest.fixture(scope='session')
def data_json():
    path = 'tests/ingestion/data/d2.json'
    data = json.loads(open(path).read())
    return data
