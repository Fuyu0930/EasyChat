import { IconButton, Box } from "@mui/material"
import { ChevronRight, ChevronLeft } from "@mui/icons-material";
import React from 'react';

type Props = {
    open: boolean;
    handleDrawerOpen: () => void;
    handleDrawerClose: () => void;
}

const DrawerToggle: React.FC<Props> = ({ open, handleDrawerClose, handleDrawerOpen }) => {
    return (
        <Box sx={{
            height: "50px",
            display: "flex",
            alignItems: "center",
            justifyContent: "center"
        }}
        >
            <IconButton onClick={open ? handleDrawerClose : handleDrawerOpen}>
                {open ? <ChevronLeft /> : <ChevronRight />}
            </IconButton>
        </Box>
    )
}
export default DrawerToggle;