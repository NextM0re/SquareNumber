import webbrowser
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from controller import router
@asynccontextmanager
async def lifespan(_: FastAPI):
    webbrowser.open('http://localhost:8000/docs')
    yield

app = FastAPI(title="Square Number", lifespan=lifespan)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app)