import React, { Component } from "react";
import ReactDOM from "react-dom";
 
 
class App extends Component {
 
  state = {
      data: ''
  };
 
    componentDidMount() {
        fetch("/api")
          .then(response => {
          return response.json();
        })
        .then(data => this.setState({ data: JSON.stringify(data)}));
  }
 
  render(){
 
      return (
            <p>Jason data = {this.state.data}</p>
      )
  }
}
 
 
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<app>, wrapper) : null;
</app>