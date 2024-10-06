import { Chip } from "@mui/material";
import { HostPort } from "types/HostPort";
import { PortBinding } from "types/PortBinding";

interface PortCellProps {
    portBindings: PortBinding[];
};

const PortCell = ({ portBindings }: PortCellProps) => {
    return (
        <>
            {portBindings.map((portBinding) => (
                portBinding.host_ports.map((hostPort: HostPort) => (
                  <Chip sx={{marginRight: 0.5}} variant="outlined" label={`${portBinding.exposed_port.port}:${hostPort.host_port}/${portBinding.exposed_port.protocol}`} />
                ))
            ))}
        </>
    )
};

export default PortCell;