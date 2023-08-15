import Link from './Link';
import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [content] = useState<string>('Learn More')
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <Link content={content}/>
      </header>
    </div>
  );
}

export default App;
