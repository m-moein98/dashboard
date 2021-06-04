import { BrowserRouter as Router, Route } from 'react-router-dom';
import Login from './components/login';
import Register from './components/register';
import Profile from './components/profile';
import Navbar from './components/navbar';

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
      </Router>
    </div>
  )
}

export default App