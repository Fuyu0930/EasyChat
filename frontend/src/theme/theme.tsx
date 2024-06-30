import { createTheme } from "@mui/material"

declare module "@mui/material/styles" {
    interface Theme {
        primaryAppBar: {
            height: number;
        };
    }
    // Make us utilize the height property
    // The question mark indicates the primaryAppBar is optional
    interface ThemeOptions {
        primaryAppBar?: {
            height: number;
        };
    }
}

export const createMuiTheme = () => {
    let theme = createTheme({
        primaryAppBar: {
            height: 50,
        },
        components: {
            MuiAppBar: {
                defaultProps: {
                    color: "default",
                    elevation: 0,
                }
            }
        }
    });

    return theme;
};


export default createMuiTheme;