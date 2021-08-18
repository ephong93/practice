import './App.css';
import Login from './pages/Login';
import Join from './pages/Join';
import Enter from './pages/Enter';
import Main from './pages/Main';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Switch>
        <Route path='/login'>
          <Login />
        </Route>
        <Route path='/join'>
          <Join />
        </Route>
        <Route path='/main'>
          <Main />
        </Route>
        <Route path='/'>
          <Enter />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
