import { useCallback, useState } from "react";

function UseCallbackResta() {
    const [a, setA] = useState(0);
    const [b, setB] = useState(0); 
  
    const total = useCallback(() => {
        console.log("Recalculando Funcion");
        return a-b;
    }, [a, b]);
    
    
    
    return (
        <>
            <h3>Calculadora de Total</h3>
            <input
                type="number"
                value={a}
                placeholder="Precio"
                onChange={(e) => setA(Number(e.target.value))}
            />
            <input
                type="number"
                value={b}
                placeholder="Cantidad"
                onChange={(e) => setB(Number(e.target.value))} // Fixed to setQty
            />
            
            <p>El total es: {total() || '0'}</p>
        </>
    );
}

export default UseCallbackResta;