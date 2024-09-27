import { ExposedPort } from "types/ExposedPort"
import { HostPort } from "types/HostPort"

export interface PortBinding {
    exposed_port: ExposedPort;
    host_ports: HostPort[];
}