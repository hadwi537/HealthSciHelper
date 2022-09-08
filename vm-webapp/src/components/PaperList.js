import React from "react";
import axios from "axios";

export default class NoteList extends React.Component {
  state = {
    reply: []
  };

  componentDidMount() {
    axios.get(`http://192.168.55.11:3000/papers`).then(res => {
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
        <ul className="list-group pt-3">
          <li className="list-group-item text-muted">No tasks to display</li>
        </ul>
      );
    } else {
      return (
        <ul className="list-group pt-3 pb-5">
          {this.state.reply.map(note => (
            <li className="list-group-item font-weight-bold" key={note._id}>
              {note.note}{" "}
              <button
                className="btn btn-link float-right p-0 text-muted"
                onClick={this.deleteOne.bind(this, note._id)}
              >
                ×
              </button>
            </li>
          ))}
        </ul>
      );
    }
  }
}