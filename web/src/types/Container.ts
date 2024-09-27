import { ExposedPort } from "types/ExposedPort"
import { PortBinding } from "types/PortBinding"

export interface Container {
    id: string;
    name: string;
    exposed_ports: ExposedPort[];
    port_bindings: PortBinding[];
}