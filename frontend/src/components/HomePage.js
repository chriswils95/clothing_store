import React, { Component } from "react";
import { Grid, Button, ButtonGroup, Typography, requirePropFactory } from "@material-ui/core";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";


export default class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      roomCode: null,
    };
    this.clearRoomCode = this.clearRoomCode.bind(this);
  }

  // async componentDidMount() {
  //   fetch("/api/user-in-room")
  //     .then((response) => response.json())
  //     .then((data) => {
  //       this.setState({
  //         roomCode: data.code,
  //       });
  //     });
  // }

  renderHomePage() {
    console.log("public is: ", process.env);
    return (
      <Grid container spacing={3}>
        <Grid item xs={12} align="center">
          <Typography variant="h3" compact="h3">
            Welcome to Chris Clothing Store
          </Typography>
        </Grid>
        <Grid item xs={12}>
          {/* <img src={require('../images/1525.jpg').default} height="100" width="100" ></img> */}
        </Grid>
      </Grid>
    );
  }

  clearRoomCode() {
    this.setState({
      roomCode: null,
    });
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route
            exact
            path="/"
            render={() => {
              return this.state.roomCode ? (
                <Redirect to={`/${this.state.roomCode}`} />
              ) : (
                this.renderHomePage()
              );
            }}
          />
        </Switch>
      </Router>
    );
  }
}