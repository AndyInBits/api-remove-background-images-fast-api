from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

app.title = "Modify Images API"
app.version = "1.0.0"

