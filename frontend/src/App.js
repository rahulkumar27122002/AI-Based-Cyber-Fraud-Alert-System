import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_BASE_URL || "http://localhost:8000";
    console.log("Using API URL:", apiUrl);

    fetch(apiUrl + "/")
      .then((res) => res.json())
      .then((data) => {
        console.log("Backend response:", data);
        setMessage(data.message || "No message in response");
      })
      .catch((err) => {
        console.error("Error fetching from backend:", err);
        setMessage("Failed to connect to backend");
      });
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Frontend is running 🚀</h1>
      <p>Message from backend: {message}</p>
    </div>
  );
}

export default App;
