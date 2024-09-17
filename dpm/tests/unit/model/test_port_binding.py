from dpm.model.exposed_port import ExposedPort
from dpm.model.host_port import HostPort
from dpm.model.port_binding import PortBinding


def test_from_kv_pair():
    """test from config"""
    exposed_port = "80/tcp"
    host_ports = [{"HostIp": "127.0.0.1", "HostPort": 8080}]
    assert PortBinding.from_kv_pair(exposed_port, host_ports) == PortBinding(
        exposed_port=ExposedPort.from_config("80/tcp"),
        host_ports=[HostPort.from_config({"HostIp": "127.0.0.1", "HostPort": 8080})]
    )


def test_list_from_config():
    """test list from config"""
    config = {"80/tcp": [{"HostIp": "127.0.0.1", "HostPort": 8080}]}
    assert PortBinding.list_from_config(config) == [
        PortBinding.from_kv_pair("80/tcp", [{"HostIp": "127.0.0.1", "HostPort": 8080}])
    ]
