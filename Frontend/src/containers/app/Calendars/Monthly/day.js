import React from 'react';

class Day extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {



    return (
      <div className = 'monthlyCalenderDay' onClick = {() => this.props.selectDay(this.props.date)}>
      {this.props.date}
      </div>

    )

  }
}


export default Day;