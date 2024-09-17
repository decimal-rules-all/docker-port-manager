from typing import List
from pydantic import BaseModel


class ExposedPort(BaseModel):
    """model for container exposed port
    """
    port: int
    protocol: str

    @staticmethod
    def from_config(config: str) -> "ExposedPort":
        """convert to exposed port from config"""
        port, protocol = config.split('/')
        return ExposedPort(port=port, protocol=protocol)

    @staticmethod
    def list_from_config(config: dict) -> List["ExposedPort"]:
        """convert to exposed port list from config"""
        return [ExposedPort.from_config(k)
                for k in config.keys()]
