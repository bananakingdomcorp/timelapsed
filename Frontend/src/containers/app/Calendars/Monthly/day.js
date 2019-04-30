import React from 'react';

class Day extends React.Component {

  render() {

    return (
      <div className = 'monthlyCalenderDay' onClick = {() => this.props.selectDay(this.props.date)}>
      {this.props.date}
      </div>


    )

  }
}


export default Day;