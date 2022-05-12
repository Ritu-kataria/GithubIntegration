import React, { useState } from "react";
import "./home.css"

function Home() {

  const [credentials, setCredentials] = useState({username: '', password: ''});

  const register = () => {
    let data=  new FormData()
    data.append("username", credentials.username)
    data.append("password", credentials.password)
    fetch('http://127.0.0.1:8000/api/users/', {
      method: 'POST',
      body: data
    }).then(
      data => (data.json())
    )
    .then(
        data => {
            console.log(data.token)
        }
    )
    .catch(error => console.error(error))
  }

  const handleChange = (event) =>{
    const register_credentials = credentials;
    register_credentials[event.target.name] = event.target.value;
    setCredentials({
      ...register_credentials
    });
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    alert('Registration Successfull')
    setCredentials({
      username: '', password: ''
    });
  }

  return (
    <div className="home">
        <div className="container col-xl-10 col-xxl-8 px-4 py-5">
    <div className="row align-items-center g-lg-5 py-5">
      <div className="col-lg-7 text-center text-lg-start">
        <h1 className="display-4 fw-bold lh-1 mb-3" style={{color: "white", fontSize: "40px"}}>Welcome to Github Issues Website!</h1>
        <p className="col-lg-10 fs-4 mt-4" style={{color: "white"}}>Get started with accessing all the issues of github repository pallets/click.</p>
      </div>
      <div className="col-md-10 mx-auto col-lg-5">
        <form className="p-4 p-md-5 border rounded-3 bg-light" onSubmit={handleSubmit} style={{boxShadow: "rgba(0, 0, 0, 0.24) 0px 3px 8px"}}>
          <div className="form-floating mb-3">
            <input name="username" type="text" className="form-control" id="floatingInput" placeholder="Username" value={credentials.username} onChange={handleChange} required/>
            <label for="floatingInput">Username</label>
          </div>
          <div className="form-floating mb-3">
            <input name= "password" type="password" className="form-control" id="floatingPassword" placeholder="Password" value={credentials.password} onChange={handleChange} required/>
            <label for="floatingPassword">Password</label>
          </div>
          <button className="w-100 btn" type="submit" onClick={register} style={{backgroundColor: "#1b1b1b", color: "white"}}>Register</button>
          <hr className="my-4" />
          <small className="text-muted">Already have an account?</small> <a href="/login" className="ml-1">login</a>
        </form>
      </div>
    </div>
  </div>

    </div>
  );
}

export default Home;
