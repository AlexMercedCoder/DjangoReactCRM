import React, { Component } from "react";
import ReactDOM from "react-dom";
 
 
export class App extends Component {
 
  state = {
      data: ''
  };
 
    componentDidMount() {
        fetch("/api/actor/")
          .then(response => {
          return response.json();
        })
        .then(data => this.setState({ data: JSON.stringify(data)}));
  }
 
  render(){
 
      return (
            <p>Jason data = {this.state.data}  test text</p>
      )
  }
}
 
 
wrapper ? ReactDOM.render(<App></App>, wrapper) : null;