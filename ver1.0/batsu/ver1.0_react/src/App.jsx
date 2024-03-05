import React from "react";
import Card from "./Card";
import "./styles.css";

// Main function
export default function App() {
  return (
    <div className="App">
      <h1>Flash Cards</h1>
      <h2>Click on a card to reveal the secret solution.</h2>
      <Card frontSide="koira" backSide="dog" />
      <Card frontSide="kissa" backSide="cat" />
      <Card frontSide="kani" backSide="rabbit" />
    </div>
  );
}
