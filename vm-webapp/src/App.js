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

            <div style = {{display: 'inline', float: 'left', textAlign: 'center'}}>
              {/* <PaperList /> */}
            </div>

          </div>
        </div>

        <div className='container'>
          <h1> Health Sci Helper! </h1>
          <p> visualising paper information </p>
          <Table />
        </div>

        <div className='container'>
          <h3> Test chart</h3>
          <Chart />
        </div>


      </div>
    );
  
    }
  }


export default App;
