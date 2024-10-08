import { Link, Tooltip } from "@mui/material";

interface IdCellProps {
  id: string;
}

const IdCell = ({ id }: IdCellProps) => {
  return (
    <Tooltip title={id} arrow>
      <Link underline="none">{id.substring(0, 12)}</Link>
    </Tooltip>
  );
};

export default IdCell;
