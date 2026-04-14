from fastapi import FastAPI

from .openapi_metadata import tags_metadata

app = FastAPI(
    title="패스트다이닝 API",
    openapi_tags=tags_metadata
)