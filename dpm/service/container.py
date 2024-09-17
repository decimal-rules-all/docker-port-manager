from typing import List

import dpm.core.container as container_core
from dpm.service.message.container import GetContainerResponse


async def get_container(container_id: str) -> GetContainerResponse:
    """get container"""
    container = container_core.get_container(container_id)
    return GetContainerResponse.from_container(container)


async def get_containers() -> List[GetContainerResponse]:
    """get containers"""
    contianers = container_core.get_containers()

    return [GetContainerResponse.from_container(c) for c in contianers]
