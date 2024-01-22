"""Module providing functions for manager docker port config"""
import argparse
import json
import os

from enum import Enum


CONTAINER_PATH = '/var/snap/docker/common/var-lib-docker/containers/'
CONFIG_FILE = 'config.v2.json'
HOSTCONFIG_FILE = 'hostconfig.json'


class Protocol(Enum):
    """Enum for supported protocol"""
    TCP = 'tcp'
    UDP = 'udp'


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

    def is_exported_port_exist(self, port: int, protocol: Protocol = Protocol.TCP) -> bool:
        """detemine if container exports the port"""
        exported_ports = self.list_exported_ports()
        return "/".join([str(port), str(protocol.value)]) in exported_ports.keys()

    def is_port_binding_exist(self, container_port:int, host_port: int,
                              protocol: Protocol = Protocol.TCP) -> bool:
        """determine if port binding exists"""
        port_bindings = self.list_port_bindings()
        host_ports = port_bindings.get("/".join([str(container_port), str(protocol.value)]), [])
        return any(p for p in host_ports if p["HostPort"] == str(host_port))

    def add_exported_port(self, port: int, protocol: Protocol = Protocol.TCP) -> None:
        """add container exported port"""
        exported_port = {"/".join([str(port), str(protocol.value)]): {}}
        self.container_config['Config']['ExposedPorts'].update(exported_port)

    def add_port_binding(self, container_port: int,
                         host_port: int, protocol: Protocol = Protocol.TCP) -> None:
        """add host port binding. will export container port if not exists."""
        # add container exported port
        self.add_exported_port(container_port, protocol=protocol)
        # add host port binding
        port_binding = {"/".join([str(container_port), str(protocol.value)]):
                        [{"HostIp": "", "HostPort": str(host_port)}]}
        self.host_config["PortBindings"].update(port_binding)

    def remove_exported_port(self, port:int, protocol: Protocol = Protocol.TCP) -> None:
        """remove container exported port"""
        exported_ports = self.list_exported_ports()
        exported_ports.pop("/".join([str(port), str(protocol.value)]), None)

    def remove_port_binding(self, container_port: int, host_port: int,
                            protocol: Protocol = Protocol.TCP) -> None:
        """remove host port binding"""
        port_bindings = self.list_port_bindings()
        host_ports = port_bindings.get("/".join([str(container_port), str(protocol.value)]), [])
        host_ports = [p for p in host_ports if not p.get("HostPort") == str(host_port)]
        if not host_ports:
            port_bindings.pop("/".join([str(container_port), str(protocol.value)]), None)
        else:
            port_bindings["/".join([str(container_port), str(protocol.value)])] = host_ports

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

    def save(self) -> None:
        """save both container config and host config"""
        self.save_container_config()
        self.save_host_config()


def main():
    """run for cli"""
    parser = argparse.ArgumentParser()
    parser.add_argument("container_id", type=str,
                        help="container id")
    subparsers = parser.add_subparsers(dest="action", help="action to perform", required=True)

    # list port binding options
    action_lst = subparsers.add_parser("list")

    # add port binding options
    action_add = subparsers.add_parser("add")
    action_add.add_argument("container_port", type=int,
                            help="container port")
    action_add.add_argument("--protocol", type=str,
                            default="tcp", choices=["tcp", "udp"],
                            help="port protocol, default tcp")
    action_add.add_argument("--host_port", type=int,
                            help="host port")

    # remove port binding options
    action_remove = subparsers.add_parser("remove")
    action_remove.add_argument("container_port", type=int,
                               help="container port")
    action_remove.add_argument("--protocol", type=str,
                               default="tcp", choices=["tcp", "udp"],
                               help="port protocol, default tcp")
    action_remove.add_argument("--host_port", type=int,
                               help="host port")

    args = parser.parse_args()

    dpm = DockerPortManager(args.container_id)

    # list port binding
    if args.action == "list":
        exported_ports = dpm.list_exported_ports()
        port_bindings = dpm.list_port_bindings()

        print("container port | protocol | host ports")
        print("-------------- | -------- | ----------")
        for k in exported_ports.keys():
            cp, proto = k.split('/')
            hp = ",".join([b.get("HostPort") for b in port_bindings.get(k, {})])
            print(f"{cp:14} | {proto:8} | {hp}")

    # add port binding
    elif args.action == "add":
        cp = args.container_port
        hp = args.host_port if args.host_port else args.container_port
        proto = Protocol.TCP if args.protocol == "tcp" else Protocol.UDP
        dpm.add_port_binding(cp, hp, protocol=proto)
        dpm.save()

    # remove port binding
    elif args.action == "remove":
        cp = args.container_port
        hp = args.host_port if args.host_port else args.container_port
        proto = Protocol.TCP if args.protocol == "tcp" else Protocol.UDP
        dpm.remove_port_binding(cp, hp, protocol=proto)
        dpm.save()


if __name__ == '__main__':
    main()
