from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fleet Tracking API is Running"}

@app.get("/health")
def health_check():
    return {"status": "Ok"}
