from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

SearchQuery = Annotated[str | None, Query(min_length=3, max_length=50)]


@app.get("/items/")
async def read_items(q: SearchQuery = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/users/")
async def read_users(q: SearchQuery = None):
    results = {"users": [{"user_id": "Rick"}, {"user_id": "Morty"}]}
    if q:
        results.update({"q": q})
    return results
