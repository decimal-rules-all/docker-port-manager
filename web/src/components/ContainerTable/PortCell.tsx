import { Chip, Tooltip } from "@mui/material";
import { HostPort } from "types/HostPort";
import { PortBinding } from "types/PortBinding";

interface PortCellProps {
  portBindings: PortBinding[];
}

const PortCell = ({ portBindings }: PortCellProps) => {
  return (
    <>
      {portBindings.map((portBinding) =>
        portBinding.host_ports.map((hostPort: HostPort) => (
          <Tooltip
            title={
              <>
                Portocol: {portBinding.exposed_port.protocol} <br />
                Exposed Port: {portBinding.exposed_port.port} <br />
                Host Port: {hostPort.host_port} <br />
                Host IP: {hostPort.host_ip}
              </>
            }
            arrow
          >
            <Chip
              sx={{ marginRight: 0.5 }}
              variant="outlined"
              label={`${portBinding.exposed_port.port}:${hostPort.host_port}/${portBinding.exposed_port.protocol}`}
            />
          </Tooltip>
        ))
      )}
    </>
  );
};

export default PortCell;
