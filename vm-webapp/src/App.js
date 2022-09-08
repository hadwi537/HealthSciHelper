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
        <div className="container">
          <div className="row">

          </div>
        </div>

        <div className='container' style = {{position: 'right'}}>
          <h1> Health Sci Helper! </h1>
          <p> Visualising paper information </p>
          <Table />
        </div>

        <div className='container' style={{width: '1200', height: '1200'}} >
          <h3> Number of Prerequistes by paper name</h3>
          <Chart />
        </div>


      </div>
    );
  
    }
  }


export default App;
