from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import dpm.service.container as container_service
from dpm.service.message.container import GetContainerResponse


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/containers", response_model=List[GetContainerResponse])
async def get_containers() -> List[GetContainerResponse]:
    """list containers"""
    return await container_service.get_containers()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
