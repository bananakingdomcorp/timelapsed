import React from 'react'
import {connect} from 'react-redux'
import Selector from './selector'
import ReactDOM from 'react-dom'
import {addTimes, removeTimes} from './../../../../modules/card'


const ModalRoot = document.querySelector('#modal-root-two')

class DailyCalendar extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      recurringTimes: [],
      times: []
    }
    this.el = document.createElement('div');
    this.dailyCalendarModalRef = React.createRef();
  }

  //state.times organized in the following way: [times, numweeks, weeksskipped]


  componentWillMount() {
    ModalRoot.appendChild(this.el)
    this.props.listenerUnLoader()
    document.addEventListener("mousedown", this.handleClickOutside)
    this.findTimes()
  }

  componentWillUnmount() {
    ModalRoot.removeChild(this.el)
    this.props.listenerLoader()
    document.removeEventListener("mousedown", this.handleClickOutside)
  }
  //Show existing times for this date. 

  findTimes = () => {

    //If we are on the monthly calendar, we may have recurring times that overlap with our current day.

    if(this.props.times[Object.keys(this.props.times)[0]] === undefined ) {
      if (this.props.times[this.props.day]) {
        this.setState({times: this.props.times[this.props.day] })
      }
      return;
    }
    let today = new Date(this.props.day)

    Object.keys(this.props.times).forEach((item) => {
      let temp = new Date(item);
      if(temp.getDay() !== today.getDay()) {
        //Do nothing
      } else {
        //We need to do some work to see if our times match up. 

        //If our date is before the date we are looking at...
        if(today < temp) {
          //Do nothing.
        } else if(temp.getTime() === today.getTime()) {
          //We are on the first date that this recurring date was created, we can edit. 
          this.setState({times: [...this.state.times, this.props.times[item][0]] })
          
        } else {
          let times = this.props.times[item][0][1] 
          while(temp < today && times > 0 ) {
            //We need to cycle through our times...
            //Adds one week. 
            temp.setDate(temp.getDate()+(7* (this.props.times[item][0][2] +1)));
            
            if(temp.getTime() === today.getTime()) {
              this.setState({recurringTimes: [...this.state.recurringTimes, this.props.times[item][0]] })
              break;
            }
            times--
          }
        }

      }
    })

  }

  handleClickOutside = (e) =>  {
    if (!this.dailyCalendarModalRef.current.contains(e.target)) {
      this.props.closeModal();

    }
  }

  convertTime =(arr) => {
    return Number(arr[0]) * 60 + Number(arr[1])
  }

  testOverlap = (next, numweeks, skipped) => {

    let overlap = false;

    let testOne = this.convertTime(next.split(',')[0].split(':'))
    let testTwo = this.convertTime(next.split(',')[1].split(':'))

    let fixed = this.state.times.map((item) => {
      let itemOne = this.convertTime(item[0].split(',')[0].split(':'))
      let itemTwo = this.convertTime(item[0].split(',')[1].split(':'))
    
      if(testOne < itemOne && testTwo > itemOne && testTwo < itemTwo) {
        //replace the first time.
        item[0].split(',')[0] = next.split(',')[0]
        overlap = true;
        return [`${next.split(',')[0]} , ${item[0].split(',')[1]}`, numweeks, skipped]
      }
      if(testOne < itemOne && testTwo > itemTwo) {
        //Replace both times
        overlap = true;
        item[0].split(',')[0] = next.split(',')[0]
        item[0].split(',')[1] = next.split(',')[1]
        return [`${next.split(',')[0]},${next.split(',')[1]}`, numweeks, skipped]
      }
    
      if(testOne > itemOne && testOne < itemTwo && testTwo > itemTwo ) {
        //Replace the last time.
        overlap = true;
        item[0].split(',')[1] = next.split(',')[1]
        return [`${item[0].split(',')[0]},${next.split(',')[1]}`, numweeks, skipped]
      }
      return item
    
    })

    return overlap? fixed: false;

  }

  resort = () => {
    let merged = [];


    
  this.state.times.forEach((item) => {
    if(merged.length === 0) {
      merged.push(item)
    } else {
      let current = merged.pop()
      let temp =this.convertTime(current[0].split(',')[1].split(':'))

      let itemFirst = this.convertTime(item[0].split(',')[0].split(':'))
      let itemSecond = this.convertTime(item[0].split(',')[1].split(':'))

      if(temp > itemFirst && temp < itemSecond  ) {
        merged.push([`${current[0].split(',')[0]},${item[0].split(',')[1]}`, item[1], item[2] ])
      } 
      if(temp > itemFirst && temp > itemSecond ) {
        merged.push(current)
      } else {
        merged.push(current, item)
      }
    }
  })

  return merged

  }



  addTime = (time, weeks, skipped) => {
    //if overlap.
    let test = this.testOverlap(time, weeks, skipped);

    if(test) {
      //Why do we sort twice here? First, we add in any overlap, resort those times (we may have added more overlap at this point), then resort again to fix any added overlap. 
      this.setState({times: test.sort((a, b) => {return  this.convertTime(a[0].split(',')[0].split(':') ) - this.convertTime(b[0].split(',')[0].split(':') ) })}, 
      () =>  {this.setState({times: this.resort()})} )

      return "Overlap"


    } else {
      //Add and sort
      this.setState({times: [...this.state.times, [time, weeks, skipped]  ]}, 
        () => this.setState({times: this.state.times.sort((a, b) => {return  this.convertTime(a[0].split(',')[0].split(':') ) - this.convertTime(b[0].split(',')[0].split(':') ) }) }, 
      ))
    }

  }

  deleteTime = (time) => {

    this.setState({times: this.state.times.filter((item) => item[0] !== time)})


  }

  submitTimes = () => {
    if (this.state.times.length !== 0) {
      this.props.addTimes(this.props.day, this.state.times)



    }
    this.props.closeModal(this.state.times)
  }


  render() {



    return ReactDOM.createPortal(
      <div className = 'dailyCalendarModal' ref = {this.dailyCalendarModalRef}>

        Recurring Times for {this.props.day}:
        {this.state.recurringTimes.map((time) => {
          let split = time[0].split(',')
          if(time[1] !== 0 && time[2] ===0) {
            return <div> Time Start: {split[0]} --- Time End: {split[1]} Repeating for {time[1]} times <span onClick = {() => this.deleteTime(time)}>Delete Time</span> </div>
          }
          if(time[1] !== 0 && time[2] !==0) {
            return <div> Time Start: {split[0]} --- Time End: {split[1]} Repeating for {time[1]} times, every {time[2]} weeks <span onClick = {() => this.deleteTime(time)}>Delete Time</span> </div>
          }
          return <div> Time Start: {split[0]} --- Time End: {split[1]} <span onClick = {() => this.deleteTime(time)}>Delete Time</span> </div>
        })}


        Existing Times for {this.props.day}:

        {this.state.times.map((time) => {
          let split = time[0].split(',')
          if(time[1] !== 0 && time[2] ===0) {
            return <div> Time Start: {split[0]} --- Time End: {split[1]} Repeating for {time[1]} times <span onClick = {() => this.deleteTime(time)}>Delete Time</span> </div>
          }
          if(time[1] !== 0 && time[2] !==0) {
            return <div> Time Start: {split[0]} --- Time End: {split[1]} Repeating for {time[1]} times, every {time[2]} weeks <span onClick = {() => this.deleteTime(time)}>Delete Time</span> </div>
          }
          return <div> Time Start: {split[0]} --- Time End: {split[1]} <span onClick = {() => this.deleteTime(time)}>Delete Time</span> </div>
        })}

        Add a time:

        <Selector addTime = {this.addTime} />

        <button onClick = {this.submitTimes}>Finished </button>
        
      </div>,
      this.el

    )
  }
}

function mapStateToProps(state) {
  return {
    times: state.card.times

  }
}

const mapDispatchToProps = {
  addTimes,
  removeTimes

}


export default connect(mapStateToProps, mapDispatchToProps) (DailyCalendar)