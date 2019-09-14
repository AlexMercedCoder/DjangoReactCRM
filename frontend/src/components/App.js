import React, { Component } from "react";
import ReactDOM from "react-dom";
import Navigation from "./Nav.js";
import DataProvider from "./dataprovider.js";
import Table from "./Table.js";
 
 
class App extends Component {
 
 
  render(){
 
      return (<div>
                <Navigation/>
               
              </div>
      )
  }
}
 
 
ReactDOM.render(<App/>, document.getElementById('app'));