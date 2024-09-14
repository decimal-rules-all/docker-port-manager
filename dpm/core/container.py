import os
import json

from typing import List


CONTAINER_PATH = '/var/lib/docker/containers'
CONFIG_FILE = 'config.v2.json'
HOSTCONFIG_FILE = 'hostconfig.json'


def load_container_config(container_id: str) -> dict:
    """load container config"""
    config_path = os.path.join(CONTAINER_PATH, container_id, CONFIG_FILE)
    with open(config_path, encoding='utf-8') as file:
        return json.load(file)


def load_host_config(container_id: str) -> dict:
    """load host config"""
    config_path = os.path.join(CONTAINER_PATH, container_id, HOSTCONFIG_FILE)
    with open(config_path, encoding='utf-8') as file:
        return json.load(file)


class Container():
    """container model
    """
    def __init__(self, container_id: str) -> None:
        self.container_id = container_id
        self.container_config = load_container_config(container_id)
        self.host_config = load_host_config(container_id)

    def get_name(self) -> str:
        """get container name"""
        return self.container_config.get('Name', '')

    def get_exported_ports(self) -> dict:
        """get exported ports"""
        return self.container_config.get('Config', {}).get('ExposedPorts', {})

    def get_port_bindings(self) -> dict:
        """get port bindings"""
        return self.host_config.get('PortBindings', {})


def get_container(container_id: str) -> Container:
    """get container by container id"""
    return Container(container_id)


def get_containers() -> List[Container]:
    """get containers"""
    container_ids = [f.name for f in os.scandir(CONTAINER_PATH) if f.is_dir()]

    return [get_container(container_id) for container_id in container_ids]
