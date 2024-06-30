import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom"
import Home from "./pages/Home.tsx";


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
  return <RouterProvider router={router} />;
}

export default App
