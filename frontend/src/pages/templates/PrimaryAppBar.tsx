import { AppBar, Toolbar, Link, Typography, Box, IconButton, Drawer, useMediaQuery } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import MenuIcon from "@mui/icons-material/Menu";
import { useState, useEffect } from "react";


const PrimaryAppBar = () => {
    const [sideMenu, setSideMenu] = useState(false);
    const theme = useTheme(); // Help grab the theme

    // Return true when above 600 px
    const isSmallScreen = useMediaQuery(theme.breakpoints.up('sm'));

    useEffect(() => {
        if (isSmallScreen && sideMenu) {
            setSideMenu(false);
        }
    }, [isSmallScreen]); // useEeffect will keep tracking the isSmallScreen value

    const toggleDrawer =
        (open: boolean) => (event: React.KeyboardEvent | React.MouseEvent) => {
            if (
                event.type === "keydown" &&
                ((event as React.KeyboardEvent).key === 'Tab' || (event as React.KeyboardEvent).key === "shift")
            ) {
                return;
            }
            setSideMenu(open);
        }

    return (
        <AppBar sx={{
            zIndex: (theme) => theme.zIndex.drawer + 2,
            backgroundColor: theme.palette.background.default,
            borderBottom: `1px solid ${theme.palette.divider}`,
        }}>
            <Toolbar
                variant="dense"
                sx={{
                    height: theme.primaryAppBar.height,
                    minHeight: theme.primaryAppBar.height,
                }}>
                <Box sx={{ display: { xs: "block", sm: "none" } }}>
                    <IconButton
                        color="inherit"
                        aria-label="open drawer"
                        edge="start" sx={{ mr: 2 }}
                        onClick={toggleDrawer(!sideMenu)}>
                        <MenuIcon />
                    </IconButton>
                </Box>
                <Drawer anchor='left' open={sideMenu} onClose={toggleDrawer(false)}>
                    {[...Array(100)].map((_, i) => (
                        <Typography key={i} paragraph>
                            {i + 1}
                        </Typography>
                    ))}
                </Drawer>

                <Link href="/" underline="none" color="inherit">
                    <Typography
                        variant="h6"
                        noWrap component="div"
                        sx={{ display: { fontWeight: 700, letterSpacing: "-0.5px" } }}>
                        EasyChat
                    </Typography>
                </Link>
            </Toolbar>
        </AppBar>
    );
};

export default PrimaryAppBar;