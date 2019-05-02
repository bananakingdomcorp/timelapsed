import React from 'react'
import {connect} from 'react-redux'
import CardEditModal from './editCard/cardEditModal';



class Card extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      editModalOpen: false,

    }
  }

  openModal = () => {
    console.log('openmodal')
    this.setState({editModalOpen: true})
  }
  closeModal = () => {
    this.setState({editModalOpen: false})
  }


  render() {

    let nextTime =  <p> No Future Dates </p>

    let today = new Date();

    let days = Infinity;

    let editable = {};

    let times = this.props.data.Times.map((item, index) => {

      //Python's Date model is one day off from that of Javascript. 
      let date = new Date(item.Begin_Date)
      date.setDate(date.getDate() + 1)

      let beginSplit = item.Begin_Time.split(":")
      let endSplit = item.End_Time.split(":")

      let temp = new Date(date.getTime());
      if(temp < today) {
        //Our date is before today. 
        let numWeeks = item.Num_Weeks;

        while(temp <today && numWeeks > 0) {
          temp.setDate(temp.getDate() + 7 * (item.Weeks_Skipped + 1))
          numWeeks--;
        }

        let diff  = Math.round((today-date)/(1000*60*60*24))
        if(diff < days) {
          days = diff;
          nextTime = <div>{temp.getMonth()}-{temp.getDate()}-{date.getFullYear()}  at {beginSplit[0]}:{beginSplit[1]}-{endSplit[0]}:{endSplit[1]} </div>
        }
      }
      editable[date.toDateString()] = [`${beginSplit[0]}:${beginSplit[1]} ,${endSplit[0]}:${endSplit[1]}`, item.Num_Weeks, item.Weeks_Skipped]
      //some formatting.
      return <div key = {index} > {date.getMonth()}-{date.getDate()}-{date.getFullYear()}  at {beginSplit[0]}:{beginSplit[1]}-{endSplit[0]}:{endSplit[1]} repeating {item.Num_Weeks} times every {item.Weeks_Skipped} weeks </div>
    })


    let modal = null;

    if(this.state.editModalOpen) {
      modal = <CardEditModal times = {times} topic = {this.props.topic} closeModal = {this.closeModal} data = {this.props.data} position = {this.props.position} editable = {editable} />
    }

    return (
      <div className = 'card'>
        <div className = 'cardEdit' onClick = {this.openModal} > ... </div>      
        <p className = 'cardTitle' > {this.props.data.Name} </p>
        Next Time:
        {nextTime} 
        {modal}
      </div>
    )
  }



}


export default connect(null, null) (Card)