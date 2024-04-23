from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def message():
    return HTMLResponse('<h1>Hello world<h1/>')