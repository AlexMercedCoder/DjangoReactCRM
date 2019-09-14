import React, { Component } from "react";
import ReactDOM from "react-dom";
 
 
class Navigation extends Component {
 
 
  render(){
 
      return (
        <nav>
        <div class="nav-wrapper maroonwhite">
          <a href="#" class="brand-logo">mercedCRM</a>
          <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="">LOGIN</a></li>
            <li><a href="">SIGN UP</a></li>
            <li><a href="">Actors</a></li>
            <li><a href="">Events</a></li>
            <li><a href="">Media</a></li>
            <li><a href="">Precinct</a></li>
            <li><a href="">Contacts</a></li>
          </ul>
        </div>
      </nav>
      )
  }
}

export default Navigation;