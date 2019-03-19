import React from 'react';
import {connect} from 'react-redux';
import AddCardModal from './addCard/addCardModal'

class AddACard extends React.Component {
  constructor(props) {
    super(props);

  }
  


  render() {

    let modalView = null;
    if (this.props.modal == true) {
      modalView = <AddCardModal closeModal = {this.props.closeModal} />
    }

    return (
      <div>
        <div className =  'topicAddCard' onClick= {this.props.openModal}>
        Add a task
        </div>
        {modalView}
      </div>

    )
  }


}


const mapStateToProps = {

}

const mapDispatchToProps = {

}




export default connect(null, null) (AddACard);