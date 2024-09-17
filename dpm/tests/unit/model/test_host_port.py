from dpm.model.host_port import HostPort


def test_from_config():
    """test from config"""
    assert HostPort.from_config({"HostIp": "127.0.0.1", "HostPort": 8080}).__dict__ == {
        "host_ip": "127.0.0.1",
        "host_port": 8080
    }


def test_list_from_config():
    """test list from config"""
    assert HostPort.list_from_config([{"HostIp": "127.0.0.1", "HostPort": 8080}]) == [
        HostPort.from_config({"HostIp": "127.0.0.1", "HostPort": 8080})
    ]
