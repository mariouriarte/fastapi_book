from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/hi/{who}")
def greet(who):
    return f"Hellow? {who}"

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    response.headers['custom'] = 'header'
    return "normal body"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
