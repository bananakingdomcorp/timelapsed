import React from 'react';
import {connect} from 'react-redux'
import {addTopic} from '../../../modules/board';
import {Api} from '../../../djangoApi';


class  AddATopic extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: ''

    }

    this.submitTopic = this.submitTopic.bind(this)
  }

  submitTopic(e) {
    e.preventDefault();

    //Call the DB first to add the topic, then add to the store. 
    let data = new FormData();
    data.append('Name', this.state.title)
    Api().post('/addtopic/', data)
    .then((res) => {
      console.log(res)

    })




    //COMMENTED OUT FOR NOW, ADD REDUX AFTER SERVER RESPONSE

    // this.props.addTopic(this.state.title);
    // this.setState({title: ''})
  }

  changeTitleValue(e) {
    this.setState({title: e})

  }

  render() {

    //Add more validation below. 

    return (
      <div className = 'card'>
        <form  className = 'addCard'>
          <input className = 'addButton' type = 'submit' value = 'Add a topic!' onClick = {this.submitTopic} />
          <input className = 'addCardTitle' placeholder = 'Enter topic name' value = {this.state.title} onChange = {(e) =>  this.changeTitleValue(e.target.value)}  required /> 

        </form>

      </div>
    )
  
  }

}

const mapDispatchToProps = {
  addTopic
}




export default connect(null, mapDispatchToProps ) (AddATopic);