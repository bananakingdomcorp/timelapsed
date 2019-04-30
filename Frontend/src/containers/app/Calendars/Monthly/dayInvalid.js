import React from 'react';

class DayInvalid extends React.Component {

  render() {

    return (
      <div className = 'monthlyCalenderPast' >
      {this.props.date}
      </div>


    )

  }
}


export default DayInvalid;