from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
	return { "message": "Hellou DevOps with Docker 2022" }


