import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from "./components/login";
import Register from "./components/register";
import Profile from "./components/profile";
import Navbar from "./components/navbar";
import Error404 from "./components/error404";

function App() {
  return (
    <div className="App">
      <Router>
        <Route path="/" exact>
          <Navbar />
          <Profile />
        </Route>
        <Route path="/login">
          <Navbar />
          <Login />
        </Route>
        <Route path="/register">
          <Navbar />
          <Register />
        </Route>
        <Route>
          <Navbar />
          <Error404 />
        </Route>
      </Router>
    </div>
  );
}

export default App;
