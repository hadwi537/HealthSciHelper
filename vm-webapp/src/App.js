import './App.css';
import { v4 as uuid } from 'uuid';
import axios from 'axios';
import React, { Component } from 'react'
import PaperList from './components/PaperList'
import Table from './components/table';
import Chart from './components/chart'


class App extends Component {

  //state object contains properties for everything to store as state
  state = {
    data: [],
    session_id: uuid(),
  };



  render() {

    return (
      <div className="App">

        <div className='container' >
        <h1> Health Sci Helper! </h1>
          <p> Visualising paper information </p>
          <h3> Number of Prerequistes by paper code</h3>
          <Chart />
        </div>

        <div className='container'>
          
          <Table />
        </div>
      </div>
    );
    }
  }




export default App;
