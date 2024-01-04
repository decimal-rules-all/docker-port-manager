"""Module providing functions for manager docker port config"""
import argparse
import json
import os


CONTAINER_PATH = '/var/snap/docker/common/var-lib-docker/containers/'
CONFIG_FILE = 'config.v2.json'
HOSTCONFIG_FILE = 'hostconfig.json'


class DockerPortManager:
    """docker port manager"""

    def __init__(self, container_id: str) -> None:
        self._container_id = container_id
        self.container_config = self.load_container_config()
        self.host_config = self.load_host_config()

    def load_container_config(self) -> dict:
        """load container config"""
        config_path = os.path.join(CONTAINER_PATH, self._container_id, CONFIG_FILE)
        with open(config_path, encoding='utf-8') as file:
            return json.load(file)

    def load_host_config(self) -> dict:
        """load host config"""
        config_path = os.path.join(CONTAINER_PATH, self._container_id, HOSTCONFIG_FILE)
        with open(config_path, encoding='utf-8') as file:
            return json.load(file)

    def list_exported_ports(self) -> dict:
        """list all exported ports"""
        return self.container_config.get('Config', {}).get('ExposedPorts', {})

    def list_port_bindings(self) -> dict:
        """list all port bindings"""
        return self.host_config.get('PortBindings', {})

    def add_exported_port(self, port: int) -> None:
        """add exported port"""
        exported_port = {str(port) + '/tcp': {}}
        self.container_config['Config']['ExposedPorts'].update(exported_port)

    def add_port_binding(self, container_port: int, host_port: int) -> None:
        """add port binding"""
        port_binding = {str(container_port) + '/tcp': [{'HostIp': '', 'HostPort': str(host_port)}]}
        self.host_config['PortBindings'].update(port_binding)

    def save_container_config(self) -> None:
        """save container config"""
        config_path = os.path.join(CONTAINER_PATH, self._container_id, CONFIG_FILE)
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(self.container_config, file)

    def save_host_config(self) -> None:
        """save host config"""
        config_path = os.path.join(CONTAINER_PATH, self._container_id, HOSTCONFIG_FILE)
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(self.host_config, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('container_id', help='container id',
                        type=str)
    args = parser.parse_args()

    dpm = DockerPortManager(args.container_id)
    print(dpm.list_exported_ports())
    print(dpm.list_port_bindings())
