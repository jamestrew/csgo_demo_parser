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


@pytest.fixture(scope='module')
def db_cur(db_conn):
    cur = db_conn.cursor()
    yield cur
    cur.close()
    db_conn.rollback()


@pytest.fixture()
def fixture_path():
    return 'tests/ingestion/fixtures'


@pytest.fixture()
def data_txt_path(fixture_path):
    return os.path.join(fixture_path, 'd2.txt')


@pytest.fixture()
def data_json_path(fixture_path):
    return os.path.join(fixture_path, 'd2.json')


@pytest.fixture()
def data_txt(data_txt_path):
    with open(data_txt_path) as txt:
        data = txt.read()
    return data


@pytest.fixture()
def data_json(data_json_path):
    data = json.loads(open(data_json_path).read())
    return data


@pytest.fixture()
def raw_match_path(fixture_path):
    return os.path.join(fixture_path, 'raw_match_data.txt')


@pytest.fixture()
def raw_match_txt(raw_match_path):
    with open(raw_match_path) as txt:
        data = txt.read()
    return data


@pytest.fixture
def item_data(fixture_path):
    path = os.path.join(fixture_path, 'item_data.txt')
    with open(path) as txt:
        data = txt.read()
    return data


@pytest.fixture
def weapons_data(fixture_path):
    path = os.path.join(fixture_path, 'weapons.json')
    with open(path) as jf:
        data = json.load(jf)
    return data


@pytest.fixture
def weapons_data_clean(fixture_path):
    path = os.path.join(fixture_path, 'weapons_clean.json')
    with open(path) as jf:
        data = json.load(jf)
    return data


@pytest.fixture
def events(fixture_path):
    path = os.path.join(fixture_path, 'events.json')
    with open(path) as jf:
        data = json.load(jf)
    return data


@pytest.fixture
def events_clean(fixture_path):
    path = os.path.join(fixture_path, 'events_clean.json')
    with open(path) as jf:
        data = json.load(jf)
    return data


@pytest.fixture
def hurt(fixture_path):
    path = os.path.join(fixture_path, 'hurt.json')
    with open(path) as jf:
        data = json.load(jf)
    return data


@pytest.fixture
def hurt_clean(fixture_path):
    path = os.path.join(fixture_path, 'hurt_clean.json')
    with open(path) as jf:
        data = json.load(jf)
    return data
