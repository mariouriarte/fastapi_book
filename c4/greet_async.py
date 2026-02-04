from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/hi-async")
async def greet():
    await asyncio.sleep(3)
    return f"Hellow? world?"

#@app.post("/hi")
#def greet_post(who:str = Body(embed=True)):
#    return f"Hello? {who}?"
#
#@app.get("/happy")
#def happy(status_code=200):
#    return ":)"
#
#@app.get("/header/{name}/{value}")
#def header(name: str, value: str, response: Response):
#    response.headers[name] = value
#    response.headers['custom'] = 'header'
#    return "normal body"
#
#
#
#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run("hello:app", reload=True)
