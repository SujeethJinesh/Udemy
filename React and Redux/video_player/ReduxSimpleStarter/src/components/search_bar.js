import React, { Component } from 'react';

//class based method. Must have a render method
//should use functional components until necessary to be class based
//only class based components have state!
class SearchBar extends Component {
  constructor(props) {
    super(props); //calling parent method
    this.state = { term: '' };
  }

  onInputChange(term) {
    this.setState({ term });
    this.props.onSearchTermChange(term);
  }

  //this.setState should be used all the time, and we want to update our state with the event obj
  render() {
    return (
      <div className="search-bar">
        <input
          value={this.state.term}
          onChange={event => this.onInputChange(event.target.value)}
        />
      </div>
    );
  }

  //event handler
  //event describes what happened, and what changed
  // onInputChange(event) {
  //     console.log(event.target.value)
  // }
}

//how to export a const
export default SearchBar;
