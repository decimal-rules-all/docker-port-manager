from typing import List
from pydantic import BaseModel


class HostPort(BaseModel):
    """model for host port
    """
    host_ip: str
    host_port: int

    @staticmethod
    def from_config(config: dict) -> "HostPort":
        """convert to host port from config"""
        return HostPort(host_ip=config.get("HostIp"),
                        host_port=config.get("HostPort"))

    @staticmethod
    def list_from_config(config: List[dict]) -> List["HostPort"]:
        """convert to host port list from config"""
        return [HostPort.from_config(d) for d in config]
