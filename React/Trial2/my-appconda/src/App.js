// import logo from './logo.svg';
// import './App.css';

// export default function Square() { // defines a fxn, Square()
//   // "export" makes function accessible outside of App.js
//   // "default" tells other files that this is main fxn in file 
//   return <button className="square">X</button> // this line returns a button with X in it
//   // <button> is a JSX element -- combo of JS and HTML
//   // className="square": button property telling CSS how to style the button
// }

// React components need to return a single JSX element, so include multiple buttons in one return fxn:
export default function Board() { // defines a fxn, Square()
  // "export" makes function accessible outside of App.js
  // "default" tells other files that this is main fxn in file 
  return (
    <>
      <div className="board-row">
        <button className="square">1</button>
        <button className="square">2</button>
        <button className="square">3</button>
      </div>
      <div className="board-row">
        <button className="square">4</button>
        <button className="square">5</button>
        <button className="square">6</button>
      </div>
      <div className="board-row">
        <button className="square">7</button>
        <button className="square">8</button>
        <button className="square">9</button>
      </div>
    </>
  );
  // <button> is a JSX element -- combo of JS and HTML
  // className="square": button property telling CSS how to style the button
}

