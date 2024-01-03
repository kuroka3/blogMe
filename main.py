from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.comment import comment_router
from domain.thread import thread_router

app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
def root():
    return {'message': 'blogMe Root'}


app.include_router(thread_router.router)
app.include_router(comment_router.router)
