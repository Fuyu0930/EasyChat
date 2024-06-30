import { AppBar, Toolbar, Link, Typography, Box, IconButton } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import MenuIcon from "@mui/icons-material/Menu";


const PrimaryAppBar = () => {
    const theme = useTheme(); // Help grab the theme
    return (
        <AppBar sx={{
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
                    <IconButton color="inherit" aria-label="open drawer" edge="start" sx={{ mr: 2 }}>
                        <MenuIcon />
                    </IconButton>
                </Box>
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