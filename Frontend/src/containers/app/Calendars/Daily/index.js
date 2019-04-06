import React from 'react'
import {connect} from 'react-redux'
import Selector from './selector'
import ReactDOM from 'react-dom'
import {addTimes} from './../../../../modules/card'


const ModalRoot = document.querySelector('#modal-root-two')

class DailyCalendar extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      times: []
    }
    this.el = document.createElement('div');
    this.dailyCalendarModalRef = React.createRef();
  }

  //When this page loads, we unload our previous modal listeners, and put some here. The ones here simply close the page if click off of.

  componentWillMount() {
    ModalRoot.appendChild(this.el)
    this.props.listenerUnLoader()
    document.addEventListener("mousedown", this.handleClickOutside)
  }

  componentWillUnmount() {
    ModalRoot.removeChild(this.el)
    this.props.listenerLoader()
    document.removeEventListener("mousedown", this.handleClickOutside)
  }
  //Show existing times for this date. 

  handleClickOutside = (e) =>  {
    if (!this.dailyCalendarModalRef.current.contains(e.target)) {
      this.props.closeModal();

    }
  }

  convertTime =(arr) => {
    return Number(arr[0]) * 60 + Number(arr[1])
  }

  testOverlap = (next) => {

    let overlap = false;

    let testOne = this.convertTime(next.split(',')[0].split(':'))
    let testTwo = this.convertTime(next.split(',')[1].split(':'))

    let fixed = this.state.times.map((item) => {
      let itemOne = this.convertTime(item.split(',')[0].split(':'))
      let itemTwo = this.convertTime(item.split(',')[1].split(':'))
    
      if(testOne < itemOne && testTwo > itemOne && testTwo < itemTwo) {
        //replace the first time.
        item.split(',')[0] = next.split(',')[0]
        overlap = true;
        return `${next.split(',')[0]} , ${item.split(',')[1]}`
      }
      if(testOne < itemOne && testTwo > itemTwo) {
        //Replace both times
        overlap = true;
        item.split(',')[0] = next.split(',')[0]
        item.split(',')[1] = next.split(',')[1]
        return `${next.split(',')[0]},${next.split(',')[1]}`    
      }
    
      if(testOne > itemOne && testOne < itemTwo && testTwo > itemTwo ) {
        //Replace the last time.
        overlap = true;
        item.split(',')[1] = next.split(',')[1]
        return `${item.split(',')[0]},${next.split(',')[1]}`    
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
      let temp =this.convertTime(current.split(',')[1].split(':'))

      let itemFirst = this.convertTime(item.split(',')[0].split(':'))
      let itemSecond = this.convertTime(item.split(',')[1].split(':'))

      if(temp > itemFirst && temp < itemSecond  ) {
        merged.push(`${current.split(',')[0]},${item.split(',')[1]}`)
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



  addTime = (time) => {
    //if overlap.
    let test = this.testOverlap(time);

    if(test) {
      //resort, then add ranges. 
      this.setState({times: test.sort((a, b) => {return  this.convertTime(a.split(',')[0].split(':') ) - this.convertTime(b.split(',')[0].split(':') ) })}, 
      () =>  {this.setState({times: this.resort()})} )

      return "Overlap"


    } else {
      //Add and sort
      this.setState({times: [...this.state.times, time  ]}, 
        () => this.setState({times: this.state.times.sort((a, b) => {return  this.convertTime(a.split(',')[0].split(':') ) - this.convertTime(b.split(',')[0].split(':') ) }) }, 
      ))
    }

  }

  deleteTime = (time) => {

    this.setState({times: this.state.times.filter((item) => item !== time)})


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
        Existing Times for {this.props.day}:

        {this.state.times.map((time) => {
          let split = time.split(',')
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

  }
}

const mapDispatchToProps = {
  addTimes

}


export default connect(mapStateToProps, mapDispatchToProps) (DailyCalendar)