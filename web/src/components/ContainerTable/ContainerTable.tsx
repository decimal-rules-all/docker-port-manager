import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from "@mui/material";
import { Container } from "types/Container";
import PortCell from "./PortCell";
import IdCell from "./IdCell";
import NameCell from "./NameCell";

interface ContainerTableProps {
  containers: Container[];
}

const ContainerTable = ({ containers }: ContainerTableProps) => {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="Containers">
        <TableHead>
          <TableRow>
            <TableCell width={100}>ID</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>Ports</TableCell>
            <TableCell>Action</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {containers.map((container) => (
            <TableRow key={container.id}>
              <TableCell component="th" scope="row">
                <IdCell id={container.id} />
              </TableCell>
              <TableCell>
                <NameCell name={container.name} />
              </TableCell>
              <TableCell>
                <PortCell portBindings={container.port_bindings} />
              </TableCell>
              <TableCell>edit</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default ContainerTable;
