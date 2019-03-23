import React from 'react'
import { Route, Link } from 'react-router-dom'
import BackGroundPage from './backGroundPage'
import { hot } from 'react-hot-loader'


class App extends React.Component {
  constructor(props) {
    super(props)
  }


  render() {
    return (
      <div className = 'background'>  
        <BackGroundPage />
      </div>
    
    )
  }


}

export default hot(module)(App)