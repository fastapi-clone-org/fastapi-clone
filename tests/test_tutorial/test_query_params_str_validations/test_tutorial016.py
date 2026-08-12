import importlib

import pytest
from fastapi.testclient import TestClient
from inline_snapshot import snapshot

from ...utils import needs_py310


@pytest.fixture(
    name="client",
    params=[
        pytest.param("tutorial016_an_py310", marks=needs_py310),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(
        f"docs_src.query_params_str_validations.{request.param}"
    )

    client = TestClient(mod.app)
    return client


def test_items_no_query(client: TestClient):
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}


def test_users_no_query(client: TestClient):
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == {"users": [{"user_id": "Rick"}, {"user_id": "Morty"}]}


def test_items_valid_query(client: TestClient):
    response = client.get("/items/", params={"q": "query"})
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
        "q": "query",
    }


def test_users_valid_query(client: TestClient):
    response = client.get("/users/", params={"q": "query"})
    assert response.status_code == 200
    assert response.json() == {
        "users": [{"user_id": "Rick"}, {"user_id": "Morty"}],
        "q": "query",
    }


@pytest.mark.parametrize("path", ["/items/", "/users/"])
def test_query_too_short(path: str, client: TestClient):
    response = client.get(path, params={"q": "ab"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_too_short",
                "loc": ["query", "q"],
                "msg": "String should have at least 3 characters",
                "input": "ab",
                "ctx": {"min_length": 3},
            }
        ]
    }


@pytest.mark.parametrize("path", ["/items/", "/users/"])
def test_query_too_long(path: str, client: TestClient):
    response = client.get(path, params={"q": "q" * 51})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "string_too_long",
                "loc": ["query", "q"],
                "msg": "String should have at most 50 characters",
                "input": "q" * 51,
                "ctx": {"max_length": 50},
            }
        ]
    }


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {"title": "FastAPI", "version": "0.1.0"},
            "paths": {
                "/items/": {
                    "get": {
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {"application/json": {"schema": {}}},
                            },
                            "422": {
                                "description": "Validation Error",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/HTTPValidationError"
                                        }
                                    }
                                },
                            },
                        },
                        "summary": "Read Items",
                        "operationId": "read_items_items__get",
                        "parameters": [
                            {
                                "required": False,
                                "schema": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "minLength": 3,
                                            "maxLength": 50,
                                        },
                                        {"type": "null"},
                                    ],
                                    "title": "Q",
                                },
                                "name": "q",
                                "in": "query",
                            }
                        ],
                    }
                },
                "/users/": {
                    "get": {
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {"application/json": {"schema": {}}},
                            },
                            "422": {
                                "description": "Validation Error",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/HTTPValidationError"
                                        }
                                    }
                                },
                            },
                        },
                        "summary": "Read Users",
                        "operationId": "read_users_users__get",
                        "parameters": [
                            {
                                "required": False,
                                "schema": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "minLength": 3,
                                            "maxLength": 50,
                                        },
                                        {"type": "null"},
                                    ],
                                    "title": "Q",
                                },
                                "name": "q",
                                "in": "query",
                            }
                        ],
                    }
                },
            },
            "components": {
                "schemas": {
                    "ValidationError": {
                        "title": "ValidationError",
                        "required": ["loc", "msg", "type"],
                        "type": "object",
                        "properties": {
                            "loc": {
                                "title": "Location",
                                "type": "array",
                                "items": {
                                    "anyOf": [{"type": "string"}, {"type": "integer"}]
                                },
                            },
                            "msg": {"title": "Message", "type": "string"},
                            "type": {"title": "Error Type", "type": "string"},
                            "input": {"title": "Input"},
                            "ctx": {"title": "Context", "type": "object"},
                        },
                    },
                    "HTTPValidationError": {
                        "title": "HTTPValidationError",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/ValidationError"
                                },
                            }
                        },
                    },
                }
            },
        }
    )
