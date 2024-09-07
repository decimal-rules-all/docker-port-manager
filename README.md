# Docker Port Manager

This tool helps to assign or remove a port mapping for an existing Docker container.

## CLI usage

### Listing current port mappings

```bash
python3 docker_port_manager.py ${container_id} list 
```

example

```bash
$ sudo python3 docker_port_manager.py 95e136d0ff88929ce0fe6b547a713d5667cb8a2d60b6c6f72c8717c6c63f8062 list

container port | protocol | host ports
-------------- | -------- | ----------
80             | tcp      | 80
```

### Adding port mapping

```bash
python3 docker_port_manager.py ${container_id} add ${port}
```

example

```bash
$ # add tcp 443:443 port mapping
$ sudo python3 docker_port_manager.py 95e136d0ff88929ce0fe6b547a713d5667cb8a2d60b6c6f72c8717c6c63f8062 add 443
$ # restart docker
$ sudo systemctl restart docker
$ # list port mapping
$ sudo python3 docker_port_manager.py 95e136d0ff88929ce0fe6b547a713d5667cb8a2d60b6c6f72c8717c6c63f8062 list

container port | protocol | host ports
-------------- | -------- | ----------
80             | tcp      | 80
443            | tcp      | 443
```

### Removing port mapping

```bash
python3 docker_port_manager.py ${container_id} remove ${port}
```

example

```bash
$ # remove tcp 443:443 port mapping
$ sudo python3 docker_port_manager.py 95e136d0ff88929ce0fe6b547a713d5667cb8a2d60b6c6f72c8717c6c63f8062 remove 443
$ # restart docker
$ sudo systemctl restart docker
$ # list port mapping
$ sudo python3 docker_port_manager.py 95e136d0ff88929ce0fe6b547a713d5667cb8a2d60b6c6f72c8717c6c63f8062 list

container port | protocol | host ports
-------------- | -------- | ----------
80             | tcp      | 80
```
