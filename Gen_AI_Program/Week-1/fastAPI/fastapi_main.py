from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI application!"
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello {name}, welcome to FastAPI!"
    }

@app.get("/weather")
def weather(city: str):
    return {
        "city": city,
        "temperature": "18°C",
        "condition": "Cloudy"
    }
