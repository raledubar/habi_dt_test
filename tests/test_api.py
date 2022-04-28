import pytest
from app import app
from handlers import check_filters
import json


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_get_resources(client):
    resp = client.get('/inmuebles')
    resources = json.loads(resp.data).get('inmuebles')
    assert type(resources[0] is dict)
    assert resp.status_code == 200
    assert type(resources) is list


def test_triple_filters(client):
    filters = {
        "city": "pereira",
        "year": "2020",
        "state": "pre_venta"
    }
    resp = client.get(
        "/inmuebles?city=%s&year=%s&state=%s" % (
            filters.get('city'),
            filters.get('year'),
            filters.get('state')
        )
    )
    resources = json.loads(resp.data).get('inmuebles')
    assert type(resources[0] is dict)
    assert resp.status_code == 200
    assert type(resources) is list
    for resource in resources:
        assert check_filters(
            resource=resource,
            filters=filters
        )


def test_single_filter(client):
    filter = {
        "state": "en_venta"
    }
    resp = client.get(
        '/inmuebles?state=%s' % (filter.get('state'))
    )
    resources = json.loads(resp.data).get('inmuebles')
    assert type(resources[0] is dict)
    assert resp.status_code == 200
    assert type(resources) is list
    assert check_filters(
        resource=resources[0],
        filters=filter
    )
