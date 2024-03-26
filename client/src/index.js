import React from "react";
import ReactDOM from "react-dom";
import "./styles.css"; // Import your Tailwind CSS styles
import App from "./components/App"; // Assuming your App component is in App.js or App.jsx
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  document.getElementById("root")
);
