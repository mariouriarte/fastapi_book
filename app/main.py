from fastapi import FastAPI
from web import explorer, creature, user, file_small
# from web import ai
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(file_small.router)
app.include_router(user.router)
# app.include_router(ai.router)

top = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=f"{top}/static", html=True), name="free")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

