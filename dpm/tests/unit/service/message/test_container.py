import mock
import pytest

from dpm.core.container import Container
from dpm.model.exposed_port import ExposedPort
from dpm.model.host_port import HostPort
from dpm.model.port_binding import PortBinding
from dpm.service.message.container import GetContainerResponse


@pytest.fixture()
@mock.patch("dpm.core.container.load_container_config")
@mock.patch("dpm.core.container.load_host_config")
def mocked_container(mock_host_config, mock_container_config) -> Container:
    """mocked container"""
    mock_host_config.return_value = {
        "NetworkMode": "bridge",
        "PortBindings": {
            "80/tcp": [{"HostIp":"127.0.0.1","HostPort":"8080"}],
            "443/tcp": [{"HostIp":"","HostPort":"8443"}],
            "53/udp": [{"HostIp":"","HostPort":"53"}]
        }
    }
    mock_container_config.return_value = {
        "ID": "ec0179b6301e60ab075d5ee2d0271af319bcff79894135818aa80fa69e15374a",
        "Config": {
            "Hostname": "ec0179b6301e",
            "ExposedPorts": {
                "80/tcp": {},
                "443/tcp": {},
                "53/udp": {}
            },
            "Image": "nginx"
        },
        "Name":"/eloquent_mahavira"
    }

    return Container('container_id')


class TestGetContainerResponse:
    """test get container response
    """
    def test_from_container(self, mocked_container):
        """test from container"""
        response = GetContainerResponse.from_container(mocked_container)
        assert response.id == 'container_id'
        assert response.exposed_ports == [
            ExposedPort(port=80, protocol='tcp'),
            ExposedPort(port=443, protocol='tcp'),
            ExposedPort(port=53, protocol='udp')
        ]
        assert response.port_bindings == [
            PortBinding(exposed_port=ExposedPort(port=80, protocol='tcp'),
                        host_ports=[HostPort(host_ip='127.0.0.1', host_port='8080')]),
            PortBinding(exposed_port=ExposedPort(port=443, protocol='tcp'),
                        host_ports=[HostPort(host_ip='', host_port='8443')]),
            PortBinding(exposed_port=ExposedPort(port=53, protocol='udp'),
                        host_ports=[HostPort(host_ip='', host_port='53')])
        ]
