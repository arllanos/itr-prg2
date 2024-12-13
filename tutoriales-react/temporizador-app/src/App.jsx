import { useState, useEffect } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [segundos, setSegundos] = useState(0);

  useEffect(() => {
    console.log("El componente se monto")

    const fx = () => {
      setSegundos((prevSegundos) => prevSegundos + 1 );
    }

    // iniciar el temporizador
    const timer = setInterval(fx, 1000);

    // funcion de limpieza: detener el temporizados al desmontar
    return () => {
      clearInterval(timer)
      console.log('El componenet se desmonto')
    };
  }, []);

  return (
    <>
      <h1>Temporizador con React</h1>
      <p className="read-the-docs">
        Segundos transcurridos: {segundos}
      </p>
    </>
  )
}

export default App;
