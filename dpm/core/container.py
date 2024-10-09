import os
import json

from enum import Enum
from typing import List


CONTAINER_PATH = '/var/lib/docker/containers'
CONFIG_FILE = 'config.v2.json'
HOSTCONFIG_FILE = 'hostconfig.json'


def load_container_config(container_id: str) -> dict:
    """load container config"""
    config_path = os.path.join(CONTAINER_PATH, container_id, CONFIG_FILE)
    with open(config_path, encoding='utf-8') as file:
        return json.load(file)


def save_container_config(container_id: str, container_config: dict) -> None:
    """save container config"""
    config_path = os.path.join(CONTAINER_PATH, container_id, CONFIG_FILE)
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(container_config, file)


def load_host_config(container_id: str) -> dict:
    """load host config"""
    config_path = os.path.join(CONTAINER_PATH, container_id, HOSTCONFIG_FILE)
    with open(config_path, encoding='utf-8') as file:
        return json.load(file)


def save_host_config(container_id: str, host_config: dict) -> None:
    """save host config"""
    config_path = os.path.join(CONTAINER_PATH, container_id, HOSTCONFIG_FILE)
    with open(config_path, 'w', encoding='utf-8') as file:
        json.dump(host_config, file)


class Protocol(Enum):
    """Enum for supported protocol"""
    TCP = 'tcp'
    UDP = 'udp'


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

    def is_exported_port_exist(self, port: int, protocol: Protocol = Protocol.TCP) -> bool:
        """detemine if container exports the port"""
        exported_ports = self.get_exported_ports()
        return "/".join([str(port), str(protocol.value)]) in exported_ports.keys()

    def add_exported_port(self, port: int, protocol: Protocol = Protocol.TCP) -> None:
        """add container exported port"""
        if self.is_exported_port_exist(port, protocol):
            return

        if 'Config' not in self.container_config:
            self.container_config['Config'] = {}
        if 'ExposedPorts' not in self.container_config['Config']:
            self.container_config['Config']['ExposedPorts'] = {}

        exported_port = {"/".join([str(port), str(protocol.value)]): {}}
        self.container_config['Config']['ExposedPorts'].update(exported_port)

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
