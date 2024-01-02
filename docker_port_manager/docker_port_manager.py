"""Module providing functions for manager docker port config"""
import argparse
import json
import os


CONTAINER_PATH = '/var/snap/docker/common/var-lib-docker/containers/'
CONFIG_FILE = 'config.v2.json'
HOSTCONFIG_FILE = 'hostconfig.json'


def list_ports(container_id: str) -> None:
    """list all ports for specific container"""
    with open(os.path.join(CONTAINER_PATH, container_id, CONFIG_FILE), encoding='utf-8') as file:
        config = json.load(file)

    exported_ports = config.get('Config', {}).get('ExposedPorts', {})
    print(exported_ports)

    with open(os.path.join(CONTAINER_PATH, container_id, HOSTCONFIG_FILE), encoding='utf-8') as file:
        hostconfig = json.load(file)

    ports = hostconfig.get('PortBindings', {})
    print(ports)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('container_id', help='container id',
                        type=str)
    args = parser.parse_args()

    list_ports(args.container_id)
