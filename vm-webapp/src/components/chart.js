import React from 'react';
import ReactECharts from 'echarts-for-react';
import axios from "axios";


const Page = (props) => {

    const all_pre_req_non_zero = props.papers?.filter((paper) => {
      if (paper.prereq_list.length > 0) {
        return paper
      }

    })
    // get the length of the data
    const pre_req_count = all_pre_req_non_zero?.map((paper) => 
        paper.prereq_list.length
    )
    //create array of paper titles
    const paper_codes = all_pre_req_non_zero?.map((paper) => 
        paper.paper_code
    )

    pre_req_count.max = function() {
      return Math.max.apply(null, this);
    }

  const options = {
    polar: {
        radius: [7, '80%']
    },
    radiusAxis: {
        max: pre_req_count.max()
    },
    angleAxis: {
        type: 'category',
        data: paper_codes,
        startangle: 75
    },
    series: [
      {
        type: 'bar',
        data: pre_req_count,
        coordinateSystem: 'polar',
        label: {
            show: 'true',
            position: 'middle',
            formatter: '{b}: {c}'
        }
      },
    ],
    tooltip: {},
  };

  return <ReactECharts option={options} style={{height:'1200px'}} />;
};

export default class Chart extends React.Component {
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
        <Page papers={this.state.reply}/>
      )
  }
}