import './App.css';
import { v4 as uuid } from 'uuid';
import axios from 'axios';
import React, { Component } from 'react'
import PaperList from './components/'

class App extends Component {

  //state object contains properties for everything to store as state
  state = {
    data: [],
    session_id: uuid(),
  };

  async componentWillMount() {
    const response = await axios.get(`http://localhost:3000/papers`);
    const json = await response.data;
    this.setState({ data: json });
  }

  render() {
    return (
      <div className="App">
        <div className="container">
          <div className="row">
            <div className="col" />
            <div className="col-lg-7">
              <PaperList />
            </div>
            <div className="col" />
          </div>
        </div>
      </div>
    );
  
    }
  }


export default App;
