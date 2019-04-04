import React from 'react'
import {connect} from 'react-redux'
import Selector from './selector'
import ReactDOM from 'react-dom'


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



  addTime = (time) => {
  
    if (!this.state.times.includes(time)) this.setState({times: [...this.state.times, time  ]},
        () => this.setState({times: this.state.times.sort((a, b) => {return  this.convertTime(a.split(',')[0].split(':') ) - this.convertTime(b.split(',')[0].split(':') ) }) }, 
          
        )) 
    else return 'Already Exists!'

  }

  deleteTime = (time) => {

    this.setState({times: this.state.times.filter((item) => item !== time)})


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

        <button>Finished </button>
        
      </div>,
      this.el

    )
  }
}

export default connect(null, null) (DailyCalendar)