import json
import mock
import pytest

import dpm.core.container as container_core

@pytest.fixture
def container_config():
    return json.loads('''
                      {
                        "ID":"ec0179b6301e60ab075d5ee2d0271af319bcff79894135818aa80fa69e15374a",
                        "Config":{
                          "Hostname":"ec0179b6301e",
                          "ExposedPorts":{
                            "80/tcp":{},
                            "443/tcp":{},
                            "53/udp":{}
                          },
                          "Image":"nginx"
                        },
                        "Name":"/eloquent_mahavira"
                      }''')

@pytest.fixture
def host_config():
    return json.loads('''
                      {
                        "NetworkMode":"bridge",
                        "PortBindings":{
                           "80/tcp":[{"HostIp":"127.0.0.1","HostPort":"8080"}],
                           "443/tcp":[{"HostIp":"","HostPort":"8443"}],
                           "53/udp":[{"HostIp":"","HostPort":"53"}]
                        }
                      }''')

@mock.patch("dpm.core.container.json.load")
@mock.patch("dpm.core.container.open")
def test_load_container_config(mock_open, mock_json_load, container_config):
    mock_json_load.return_value = container_config
    config = container_core.load_container_config('container_id')
    mock_open.assert_called_once()
    assert config == container_config

@mock.patch("dpm.core.container.json.load")
@mock.patch("dpm.core.container.open")
def test_load_host_config(mock_open, mock_json_load, host_config):
    mock_json_load.return_value = host_config
    config = container_core.load_container_config('container_id')
    mock_open.assert_called_once()
    assert config == host_config


class TestContainer:

    @mock.patch("dpm.core.container.json.load")
    @mock.patch("dpm.core.container.open")
    def test_get_name(self, _, mock_json_load, container_config):
        mock_json_load.return_value = container_config
        container = container_core.Container('container_id')
        assert container.get_name() == '/eloquent_mahavira'

    @mock.patch("dpm.core.container.json.load")
    @mock.patch("dpm.core.container.open")
    def test_get_exported_ports(self, _, mock_json_load, container_config):
        mock_json_load.return_value = container_config
        container = container_core.Container('container_id')
        assert container.get_exported_ports() == {'80/tcp': {}, '443/tcp': {}, '53/udp': {}}

    @mock.patch("dpm.core.container.json.load")
    @mock.patch("dpm.core.container.open")
    def test_get_port_bindings(self, _, mock_json_load, host_config):
        mock_json_load.return_value = host_config
        container = container_core.Container('container_id')
        assert container.get_port_bindings() == {
            '80/tcp': [{'HostIp': '127.0.0.1', 'HostPort': '8080'}],
            '443/tcp': [{'HostIp': '', 'HostPort': '8443'}],
            '53/udp': [{'HostIp': '', 'HostPort': '53'}]}
