import React, { useState } from "react";
import "./login.css"

function Login() {
  const [credentials, setCredentials] = useState({ username: '', password: '' });

  const login = () => {
    let data = new FormData()
    data.append("username", credentials.username)
    data.append("password", credentials.password)
    fetch('http://127.0.0.1:8000/auth/', {
      method: 'POST',
      body: data
    }).then(
      data => {
        console.log(data);
      }
    ).catch(error => console.error(error))
  }

  const handleChange = (event) => {
    const login_credentials = credentials;
    login_credentials[event.target.name] = event.target.value;
    setCredentials({
      ...login_credentials
    });
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    alert('Login Successfull')
    setCredentials({
      username: '', password: ''
    });
}

  return (
    <div id="main-wrapper" className="container" style={{marginTop: "20px"}}>
      <div className="row justify-content-center">
        <div className="col-xl-10">
          <div className="card border-0" style={{boxShadow: "rgba(0, 0, 0, 0.24) 0px 3px 8px"}}>
            <div className="card-body p-0">
              <div className="row no-gutters">
                <div className="col-lg-6">
                  <div className="p-5">
                    <div className="mb-5">
                      <h3 className="h4 font-weight-bold text-theme">Login</h3>
                    </div>
                    <h6 className="h5 mb-0">Welcome back!</h6>
                    <p className="text-muted mt-2 mb-5">Enter your username and password to access github issues.</p>
                    <form onSubmit={handleSubmit}>
                      <div className="form-group">
                        <label for="exampleInputEmail1"><i class="fa-solid fa-user"></i> &nbsp;Username</label>
                        <input type="text" className="form-control" name="username" placeholder="Enter your username" value={credentials.username} onChange={handleChange} required="True"/>
                      </div>
                      <div className="form-group mb-5 mt-3">
                        <label for="exampleInputPassword1"><i class="fa-solid fa-key"></i> &nbsp;Password</label>
                        <input type="password" className="form-control" name="password" placeholder="Enter your passsword" value={credentials.password} onChange={handleChange} required="True"/>
                      </div>
                      <button type="submit" className="btn btn-theme" onClick={login}>Login</button>
                    </form>
                  </div>
                </div>
                <div className="col-lg-6 d-none d-lg-inline-block">
                  <div className="account-block rounded-right">
                    <img alt="" src="https://cdn.dribbble.com/users/132296/screenshots/15920923/codespaces-illustration-dribbble_4x_4x.png" style={{width: "100%", height: "100%"}}/>
                    <div className="overlay rounded-right"></div>
                    <div className="account-testimonial">
                      <h4 className="text-white mb-4"></h4>
                      <p className="lead text-white"></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <p className="text-muted text-center mt-3 mb-0">Don't have an account? <a href="/" className="ml-1">register</a></p>
        </div>
      </div>
    </div>
  );
}

export default Login;
