from typing import List
from pydantic import BaseModel
from dpm.core.container import Container
from dpm.model.exposed_port import ExposedPort
from dpm.model.port_binding import PortBinding


class GetContainerResponse(BaseModel):
    """model for get container response
    """
    id: str
    name: str
    exposed_ports: List[ExposedPort]
    port_bindings: List[PortBinding]

    @staticmethod
    def from_container(container: Container) -> "GetContainerResponse":
        """convert container to get container response"""
        return GetContainerResponse(
            id=container.container_id,
            name=container.get_name(),
            exposed_ports=ExposedPort.list_from_config(container.get_exported_ports()),
            port_bindings=PortBinding.list_from_config(container.get_port_bindings())
        )
