import React from 'react';

class Day extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className = 'recurringCalenderDay'>
      {this.props.name}
      </div>

    )

  }
}


export default Day;