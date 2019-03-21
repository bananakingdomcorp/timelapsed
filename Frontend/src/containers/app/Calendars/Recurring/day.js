import React from 'react';

class Day extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {

    if(this.props.selected.contains(this.props.name)) {
      
    }

    return (
      <div className = 'recurringCalenderDay'>
      {this.props.name}
      </div>

    )

  }
}


export default Day;