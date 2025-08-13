from fastapi import FastAPI

app = FastAPI(title="product-service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/products")
def list_products():
    return [
        {"id": 1, "name": "Widget", "price": 9.99},
        {"id": 2, "name": "Gadget", "price": 14.99},
    ]
