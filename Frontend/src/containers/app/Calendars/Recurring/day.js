import React from 'react';

class Day extends React.Component {

  render() {



    return (
      <div className = 'recurringCalenderDay' onClick = {() => this.props.selectDay(this.props.name)}>
      {this.props.name}
      </div>

    )

  }
}


export default Day;