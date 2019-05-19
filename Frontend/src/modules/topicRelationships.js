//We need to have topic relationships different than cardRelationships since they may have overlapping id's. 

const inititalState = {
  relationships : {

  }
}

export default (state = inititalState, action) => {
  switch(action.type) {


    default:
      return state
  }
}