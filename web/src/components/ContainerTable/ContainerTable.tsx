import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from "@mui/material";
import { Container } from "types/Container";
import PortCell from "./PortCell";
import IdCell from "./IdCell";

const ContainerTable = ({rows}: {rows: Container[]}) => {
    return (
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="Containers">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Name</TableCell>
              <TableCell>Ports</TableCell>
              <TableCell>Action</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row.id}
              >
                <TableCell component="th" scope="row">
                    <IdCell id={row.id} />
                </TableCell>
                <TableCell>{row.name}</TableCell>
                <TableCell>
                    <PortCell portBindings={row.port_bindings} />
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