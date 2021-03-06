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

      //Python's Date model is one day off and one month off from that of Javascript. 
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
      } 

      let diff  = Math.round((temp - today)/(1000*60*60*24))

      if(diff < days) {
        days = diff;
        nextTime = <div>{temp.getMonth() + 1}-{temp.getDate()}-{date.getFullYear()}  at {beginSplit[0]}:{beginSplit[1]}-{endSplit[0]}:{endSplit[1]} </div>
      }
      //Our editable prebuilds the potential redux state that we would use if we choose to edit the times on this card.

      //We do this now simply because we don't want to have to keep going through the times. This allows this to be done a single time. 

      if (editable[date.toDateString()] === undefined) {
        editable[date.toDateString()] = [];
      }
      editable[date.toDateString()].push([`${beginSplit[0]}:${beginSplit[1]} , ${endSplit[0]}:${endSplit[1]}`, item.Num_Weeks, item.Weeks_Skipped, item.id])
      //some formatting.
      return <div key = {index} > {date.getMonth() +1}-{date.getDate()}-{date.getFullYear()}  at {beginSplit[0]}:{beginSplit[1]}-{endSplit[0]}:{endSplit[1]} repeating {item.Num_Weeks} times every {item.Weeks_Skipped} weeks </div>
    })


    let modal = null;

    if(this.state.editModalOpen) {
      modal = <CardEditModal iteratableTimes = {times} topic = {this.props.topic} closeModal = {this.closeModal} data = {this.props.data} position = {this.props.position} editable = {editable} />
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