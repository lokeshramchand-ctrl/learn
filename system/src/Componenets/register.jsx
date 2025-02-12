import React, { useState } from "react";
import axios from "axios";

const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");  // Added email state
  const [role, setRole] = useState("");  // Added role state

  const handleRegister = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/register/", {
        username,
        password,
        email,
        role,
      });
      console.log("Registration successful:", response.data);
    } catch (error) {
      console.error("Registration failed:", error);
    }
  };

  return (
    <div>
      <h1>Register</h1>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <input
        type="email"  // Set type as email for email input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}  // Update email value
      />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
};

export default Register;
