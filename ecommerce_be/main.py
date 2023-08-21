from fastapi import FastAPI


def start_application():
    app = FastAPI(title="Ecommerce", version="1.0")
    return app

app = start_application()


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
