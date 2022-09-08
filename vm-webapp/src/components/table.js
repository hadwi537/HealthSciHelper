import React, { Component } from 'react'
import axios from "axios";


// table header (simple component)
const TableHeader = () => {
    return (
      <thead>
        <tr>
          <th>Paper Code</th>
          <th>year</th>
          <th> Prerequistes </th>
        </tr>
      </thead>
    )
}

// table body (simple component)
const TableBody = (props) => {
  const rows = props.characterData.map((paper) => {
    return (
        <tr key={paper.paper_code}>
        <td>{paper.title}</td>
        <td>{paper.year}</td>
        <td>{paper.prereq_list.map(paper_code => (
          <td> {paper_code} </td>
        ))}</td>
      </tr>
    )
  })

  return <tbody>{rows}</tbody>
}

export default class Table extends React.Component {
    state = {
      reply: []
    }
    componentDidMount() {
      axios.get(`http://192.168.2.14:5000/papers`).then(res => {
        const reply = res.data;
        console.log(reply);
        this.setState({ reply });
      });
    }
    render() {
      return (
        <table>
          <TableHeader />
          <TableBody characterData={this.state.reply} />
        </table>
      )
  }
}

