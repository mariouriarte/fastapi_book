from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/{who}")
def greet(who):
    return f"Hellow? {who}"

@app.get("/happy")
def happy(status_code=200):
    return ":)"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
