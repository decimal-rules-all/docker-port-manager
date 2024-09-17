from typing import List
from pydantic import BaseModel
from dpm.model.exposed_port import ExposedPort
from dpm.model.host_port import HostPort


class PortBinding(BaseModel):
    """model for host port binding
    """
    exposed_port: ExposedPort
    host_ports: List[HostPort]

    @staticmethod
    def from_kv_pair(k: str, v: List[dict]) -> "PortBinding":
        """convert to port binding from kv pair"""
        return PortBinding(
            exposed_port=ExposedPort.from_config(k),
            host_ports=HostPort.list_from_config(v)
        )

    @staticmethod
    def list_from_config(config: dict) -> List["PortBinding"]:
        """convert to port binding list from config"""
        return [PortBinding.from_kv_pair(k, v)
                for k, v in config.items()]
