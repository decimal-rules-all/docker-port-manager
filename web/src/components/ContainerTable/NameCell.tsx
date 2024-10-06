import { Link, Tooltip } from "@mui/material";

interface NameCellProps {
    name: string;
};

const NameCell = ({ name }: NameCellProps) => {
    const nameAfterSlash = name.split('/').pop();
    return (
        <Tooltip title={name} arrow>
            <Link underline="none">{nameAfterSlash}</Link>
        </Tooltip>
    )
};

export default NameCell;