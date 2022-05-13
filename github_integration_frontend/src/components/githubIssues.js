import React, {useState, useEffect} from "react";
import "./githubIssues.css"

function GithubIssues() {

  const [issueApiData,setissueApiData] = useState([]);

    const fetchData =()=>{
        fetch("http://localhost:8000/api/issues")
        .then((response) =>{
            return response.json();
        }).then((data)=>{
            setissueApiData(data)
        })
    }
    useEffect(()=>{
        fetchData();
    },[])
    return (
      <div className="container issuescontainer mt-4">
        <div className="clearfix">
        <h1 className="text-center text-xl font-bold mb-4">Welcome, Here is the list of all the issues of repository pallet/click</h1>
        <div className="row">
          {issueApiData?.issues?.map((data) => {
            let labels = issueApiData.labels.filter((ins) => ins.reference_id == data.issue_id)
            let assignees = issueApiData.assignees.filter((ins) =>ins.reference_id == data.issue_id)
            console.log('--data',data)
            console.log('--labels',labels)
            console.log('--assignees',assignees)
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
                    Issue Title : {data.title} <br/><br />
                    State : {data.state} <br/><br />
                    Labels : {labels.length !== 0 ? labels?.map((label) =>{
                      return(<span key={label.id}>{label.name}</span>
                    )}) : "No Labels"} <br/><br />
                    Assignees : {assignees.length !== 0 ? assignees?.map((assignee) =>{
                      return(<span key={assignee.id}>{assignee.name}</span>
                    )}) : "No Assignees"}
                  </h5>
                </div>
              </div>
            </div>
          )})}
        </div>
        </div>
      </div>
    );
}

export default GithubIssues;
