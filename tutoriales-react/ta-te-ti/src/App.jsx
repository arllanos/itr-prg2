import { useState } from 'react'
import './App.css'

function App() {
  const [board, setBoard] = useState(Array(3).fill(null).map(() => Array(3).fill(null)))

  return (
    <>
      <h1>Ta-Te-Ti</h1>
      <div className='board'>
        {board.map((row, rowIndex) => (
            <div key={rowIndex} className='row'>
              {row.map((cell, cellIndex) => (
                <button key={cellIndex} className='celda'>
                  {cell}
                </button>
              ))}
            </div>
        ))}
      </div>
    </>
  )
}

export default App
