import corporate_bullshit
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

with open("index.html") as html_file:
    page_content = html_file.read()

app = FastAPI()
app.mount(f"/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount(f"/css", StaticFiles(directory="css"), name="css")


@app.get("/")
async def main_site():
    """How did you get here?"""

    bullshit = corporate_bullshit.sentence()
    to_send = page_content.replace(r"%spicy_bullshit%", bullshit)

    return HTMLResponse(content=to_send)
