from dpm.model.exposed_port import ExposedPort


def test_from_config():
    """test from config"""
    assert ExposedPort.from_config("80/tcp").__dict__ == {
        "port": 80,
        "protocol": "tcp"
    }


def test_list_from_config():
    """test list from config"""
    assert ExposedPort.list_from_config({"80/tcp": []}) == [
        ExposedPort.from_config("80/tcp")
    ]
