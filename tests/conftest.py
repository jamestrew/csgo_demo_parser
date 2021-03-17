import pytest


def pytest_addoption(parser):
    parser.addoption('--ingestion', action='store_true',
                     help='run only tests which temporarily ingests into db')
    parser.addoption('--integration', action='store_true',
                     help='run integration test')


def pytest_runtest_setup(item):
    if 'ingestion' in item.keywords and not item.config.getvalue('ingestion'):
        pytest.skip("need --ingestion option to run")
    if 'integration' in item.keywords and not item.config.getvalue('integration'):
        pytest.skip("need --integration option to run")
