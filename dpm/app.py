from typing import List
from fastapi import FastAPI

import dpm.service.container as container_service
from dpm.service.message.container import GetContainerResponse


app = FastAPI()


@app.get("/containers", response_model=List[GetContainerResponse])
async def get_containers() -> List[GetContainerResponse]:
    """list containers"""
    return await container_service.get_containers()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
