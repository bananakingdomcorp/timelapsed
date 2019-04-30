import React from 'react'
import BackGroundPage from './backGroundPage'
import { hot } from 'react-hot-loader'


class App extends React.Component {


  render() {
    return (
      <div className = 'background'>  
        <BackGroundPage />
      </div>
    
    )
  }


}

export default hot(module)(App)