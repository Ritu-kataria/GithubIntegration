import React, { useState, useEffect } from "react";
import "./githubIssues.css"

function GithubIssues() {

  const [issueApiData, setissueApiData] = useState([]);
  const [filterData, setFilterData] = useState([]);

  const fetchData = () => {
    fetch("http://localhost:8000/api/issues")
      .then((response) => {
        return response.json();
      }).then((data) => {
        setissueApiData(data)
        setFilterData(data?.issues)
      })
  }

  useEffect(() => {
    fetchData();
  }, [])

  const filteredData = (e) => {
    let value = e.target.value
    console.log('---value', value)
    if (!value){
      setFilterData(issueApiData?.issues)
      return
    }
    let data = issueApiData.issues.filter((itm) => itm.state == value)
    setFilterData(data)
  }

  return (
    <div className="container issuescontainer mt-4">
      <div className="clearfix">
        <h1 className="text-center text-xl font-bold mb-4">Welcome, Here is the list of all the issues of repository pallet/click</h1>
        <div>
          <label className="m-2">Filter Issues: </label>
          <select id="state" onChange={(_) => {
            filteredData(_)
          }}>
            <option value="">state</option>
            <option value="closed">closed</option>
            <option value="open">open</option>
          </select>
        </div>
        <div className="row">
          {filterData?.map((data) => {
            let labels = issueApiData.labels.filter((ins) => ins.reference_id == data.issue_id)
            let assignees = issueApiData.assignees.filter((ins) => ins.reference_id == data.issue_id)
            return (
              <div className="col-md-4 animated fadeIn" key={data.id}>
                <div className="card issuecard">
                  <div className="card-body">
                    <div className="issuecard-id">
                      <h1 className="text-center">
                        Issue ID : {data.issue_id}
                      </h1>
                    </div>
                    <h5 className="issuecard-title ml-0">
                      Issue Title : {data.title} <br /><br />
                      State : {data.state} <br /><br />
                      Labels : {labels.length !== 0 ? labels?.map((label) => {
                        return (<span key={label.id}>{label.name}</span>
                        )
                      }) : "No Labels"} <br /><br />
                      Assignees : {assignees.length !== 0 ? assignees?.map((assignee) => {
                        return (<span key={assignee.id}>{assignee.name}</span>
                        )
                      }) : "No Assignees"} <br /><br />
                      Created At: {data.created_at.substring(0, 10)}
                    </h5>
                  </div>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  );
}

export default GithubIssues;
