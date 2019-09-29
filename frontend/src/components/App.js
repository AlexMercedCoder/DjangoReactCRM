import React, { Component } from "react";
import ReactDOM from "react-dom";
import Navigation from "./Nav.js";
import Navigation from "./actors.js";
import Navigation from "./contacts.js";
import Navigation from "./events.js";
import Navigation from "./login.js";
import Navigation from "./media.js";
import Navigation from "./precint.js";
import Navigation from "./signup.js";
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