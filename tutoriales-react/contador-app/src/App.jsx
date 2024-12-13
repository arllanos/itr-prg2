import React, { useState } from 'react'

function App() {
  const [contador, setContador] = useState(0)

  const incrementar = () => {
    setContador((valorActual) => valorActual + 1);
  }

  const decrementar = () => {
    setContador((valorActual) => valorActual - 1);
  }

  const resetear = () => {
    setContador(0);
  }

  return (
      <div style={{ textAlign: 'center', marginTop: '50px' }}>
        <h1>Contador de React</h1>
        <p>Valor del Contador: {contador}</p>
        <button onClick={incrementar}>Incrementar</button>
        <button onClick={decrementar}>Decrementar</button>
        <button onClick={resetear}>Resetear</button>
      </div>
  )
}

export default App
