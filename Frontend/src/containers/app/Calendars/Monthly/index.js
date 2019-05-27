//This component primarially holds everything in our calendar. 


//Since this may take a while to load, try react.lazy to load this with the modal.

import React from 'react';

import {connect} from 'react-redux';

import Day from './day'

import DayInvalid from './dayInvalid'

import DailyCalendar from './../Daily/index'

import {removeTimes} from './../../../../modules/card'

class MonthlyCalender extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      numdays: 0,
      dailyCalendarOpen: false,
      currentDay: '',
      startDate: '',
      spaceDays: 0,
      currentDate: 0,
      currentMonth: 0,
      currentYear: 0,
      days: []

    }
    this.months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  }

  componentWillMount() {
    let d = new Date();
    let r = new Date(d.getFullYear(), d.getMonth() +1, 0).getDate()
    let p = new Date(d.getFullYear(), d.getMonth(), 1).getDay()

    this.setState({startDate: d, numDays : r, spaceDays: p, currentDate: d.getDate(), currentMonth: d.getMonth(), currentYear: d.getFullYear()}, ()=> this.renderCalendar())

  }

  selectDay =(day) =>  {
    //Once a day has been selected, open the daily calendar. 
    
    this.setState({dailyCalendarOpen: true})
    
    //Get the full date of this day, add to state. 

    let selected = new Date(this.state.currentYear, this.state.currentMonth, day).toDateString();

    this.setState({currentDay: selected});



  }

  increaseMonth = () =>  {

    if (this.state.currentMonth === 11) {
      //Advance the year. 
      this.increaseYear()
      this.setState({currentMonth: 0}, () => this.calculateDays())

    } else {
      this.setState({currentMonth: this.state.currentMonth + 1}, () => this.calculateDays());
    }

  }

  decreaseMonth =() =>  {

    if(this.state.currentMonth <= this.state.startDate.getMonth() && this.state.currentYear <= this.state.startDate.getFullYear() ) {
      return 
      //We can not go to previous months. 

    }

    if (this.state.currentMonth === 0) {
      this.decreaseYear()
      this.setState({currentMonth: 11}, () => this.calculateDays())
    } else {
      this.setState({currentMonth: this.state.currentMonth -1}, () => this.calculateDays())
    }

  }

  increaseYear=() =>  {
    this.setState({currentYear: this.state.currentYear +1}, () => this.calculateDays())

  }

  decreaseYear=() => {
    this.setState({currentYear: this.state.currentYear -1}, () => this.calculateDays())

  }

  calculateDays=() => {
    let r =  new Date(this.state.currentYear, this.state.currentMonth +1, 0).getDate()
    let p =  new Date(this.state.currentYear, this.state.currentMonth, 1).getDay()

    this.setState({numDays :r, spaceDays: p}, () => this.renderCalendar())

  }

  timesSort = (times) => {
    //Sort out times here.
    return Object.keys(times).sort((a, b) => new Date(a) - new Date(b)).map((item) => times[item].sort((a, b) => a[0].split(',')[0] - b[0].split(',')[0]).map((time, index) => {
      if (time[1] !== 0 && time[2] ===0) {
        return <div key = {index}> {item}, {time[0].split(',')[0]}--{time[0].split(',')[1]}, repeating for {time[1]} times <span onClick = {() => this.deleteTime(item, time)} > Delete Time </span> </div>
      }
      if (time[1] !== 0 && time[2] !==0 ) {
        return <div key = {index}> {item}, {time[0].split(',')[0]}--{time[0].split(',')[1]}, repeating for {time[1]} times every {time[2]} weeks <span onClick = {() => this.deleteTime(item, time)} > Delete Time </span>  </div>
      }
      return <div key = {index}> {item}, {time[0].split(',')[0]}--{time[0].split(',')[1]} <span onClick = {() => this.deleteTime(item, time)} > Delete Time </span>  </div> 
      }         
    ))    
  }

  renderCalendar=() => {
    let arr = []

    for (let i = 0; i < this.state.spaceDays; i++) {
      arr.push(<DayInvalid date = {''} /> )
    }

    for(let i = 1; i <= this.state.numDays; i++) {
      if(i < this.state.currentDate && this.state.currentMonth === this.state.startDate.getMonth() && this.state.currentYear === this.state.startDate.getFullYear()) {
        arr.push(<DayInvalid date = {i} />)
      } else {
        arr.push(<Day date = {i} selectDay = {this.selectDay} />)
      }
    }
    this.setState({days: arr});


  }

  closeModal = () => {
    this.setState({dailyCalendarOpen: false})
  }

  deleteTime = (day, time) => {
    this.props.removeTimes(day, time)

  }


  render () {
    let dailyCalender = null;


    if (this.state.dailyCalendarOpen === true) {

      dailyCalender = <DailyCalendar closeModal = {this.closeModal} day = {this.state.currentDay} listenerLoader = {this.props.listenerLoader} listenerUnLoader = {this.props.listenerUnLoader} />

    }

    //Shows all of our currently selected days. 

    //These need to be reorganized so that they are in correct order. 

    let dates = this.timesSort(this.props.times)





    return (
      <div>
        <div className = 'monthlyCalendarHeader'> 
          <button onClick = {this.decreaseMonth}> <i className = 'arrowLeft'></i> </button>  
          {this.months[this.state.currentMonth]}, {this.state.currentYear}  
          <button onClick = {this.increaseMonth}> <i className = 'arrowRight'></i> </button>          
        </div>
        <div className = 'monthlyCalendar'>



          {this.state.days}
          
        </div>

        {dailyCalender}
        <div className = 'MonthlyCalendarDates'>
        {dates}
        </div>
      </div>
    )
  }

}

function mapStateToProps(state) {
  return {
    times: state.card.times

  }
}

const mapDispatchToProps = {
  removeTimes,
}


export default connect(mapStateToProps, mapDispatchToProps) (MonthlyCalender);