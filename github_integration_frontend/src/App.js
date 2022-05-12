import './App.css';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import Login from "./components/login"
import GithubIssues from './components/githubIssues';
import Home from './components/home';

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="login" element={<Login />} />
      <Route path="githubIssues" element={<GithubIssues />} />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
