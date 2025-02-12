import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Login from './Components/login'; 
import Register from './Components/register'; // Corrected path for your Register component

function App() {
  return (
    <Router>
      <Routes>
        {/* Define the route for the Register page */}
        <Route path="/register" element={<Register />} />
        
        {/* Define the route for the Login page */}
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
