import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Signup from './Signup';
import Login from './Login';
import Logout from './Logout';
import ReviewForm from './ReviewForm';
import ServiceList from './ServiceList';
import Home from './Home';
import SearchFilter from './SearchFilter';

const App = () => {
  return (
    <Router>
      <div className="container mx-auto px-4">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/signup">
            <Signup />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/logout">
            <Logout />
          </Route>
          <Route path="/review">
            <ReviewForm />
          </Route>
          <Route path="/services">
            <ServiceList />
          </Route>
          <Route path="/search">
            <SearchFilter />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
