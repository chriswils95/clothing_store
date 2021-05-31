import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import ItemPage from "./ItemPage"
import ItemsPage from "./ItemsPage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <ItemsPage />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);