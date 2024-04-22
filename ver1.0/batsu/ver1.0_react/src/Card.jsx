import React, { useState } from "react";

// Card function
export default function Card({ frontSide, backSide }) {
  const [isFront, changeFace] = useState(true);
  // handleClick function
  function handleClick() {
    changeFace((oldState) => !oldState);
  }
  const text = isFront ? frontSide : backSide;
  const sideClass = isFront ? "front" : "back";
  const classList = `flash-card ${sideClass}`;
  return (
    <div className={classList} onClick={handleClick}>
      {text}
    </div>
  );
}
