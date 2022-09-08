import React from "react";
import axios from "axios";


export default class NoteList extends React.Component {
  state = {
    reply: []
  };

  componentDidMount() {
    axios.get(`http://192.168.2.14:5000/papers`).then(res => {
      const reply = res.data;
      console.log(reply);
      this.setState({ reply });
    });
  }


  render() {
    if (
      this.state.reply === undefined ||
      this.state.reply === 0 ||
      this.state.reply.length === 0
    ) {
      return (
        <ul className="paper-group pt-3">
          <li className="paper-group-item text-muted">No papers to display</li>
        </ul>
      );
    } else {
      return (
        <ul className="paper-group pt-3 pb-5">
          {this.state.reply.map(paper => (
            <li className="paper-group-item font-weight-bold" key={paper.paper_code}>
              {paper.paper}{" "}
              
            </li>
          ))}
        </ul>
      );
    }
  }
}