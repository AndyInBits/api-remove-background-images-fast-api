from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

app.title = "Modify Images API"
app.version = "1.0.0"

@app.get("/", tags=['home'])
def read_root():
    return {"Hello": "World"}