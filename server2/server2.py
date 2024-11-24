from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main():
    with open("./server2.html", "r") as html_file:
        html_return = html_file.read()
    return html_return