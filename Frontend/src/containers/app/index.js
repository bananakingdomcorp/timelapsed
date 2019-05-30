import React from 'react'
import BackGroundPage from './backGroundPage'
import ElasticPage from './../../testPages/elasticsearchTest'
import { hot } from 'react-hot-loader'
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


class App extends React.Component {


  render() {
    return (
      <div className = 'background'>  
        <Router>
          <Switch>
            <Route exact path="/" component={BackGroundPage} />
            <Route exact path='/elastictest' component={ElasticPage} />
          </Switch>
        </Router>
      </div>
    
    )
  }


}

export default hot(module)(App)