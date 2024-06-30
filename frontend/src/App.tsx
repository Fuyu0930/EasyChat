import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom"
import Home from "./pages/Home.tsx";
import { ThemeProvider } from "@emotion/react";
import { createMuiTheme } from "./theme/theme.tsx";


const router = createBrowserRouter(
  // path is the url link to achieve the component
  createRoutesFromElements(
    <Route>
      <Route path='/' element={<Home />} />
    </Route>
  )
);

// App is a React.FC type
const App = () => {
  const theme = createMuiTheme();
  return (
    <ThemeProvider theme={theme}>
      <RouterProvider router={router} />
    </ThemeProvider>
  );
}

export default App
