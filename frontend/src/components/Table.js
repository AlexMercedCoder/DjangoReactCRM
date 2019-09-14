import React, { Component } from "react";
import ReactDOM from "react-dom";
 
 
class Table extends Component {
 
 
  render(){
 
      return (
        <div>
            fetch('http://example.com/movies.json')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(JSON.stringify(myJson));
  });
        </div>
      )
  }
}

export default Navigation;
