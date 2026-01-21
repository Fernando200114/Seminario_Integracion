import { useMemo, useState } from "react";

function UseStateSuma() {
    const [price, setPrice] = useState(0);
    const [qty, setQty] = useState(0); 
  
    const total = useMemo(() => {
        console.log("Recalculando el total");
        return price * qty;
    }, [price, qty]);
    return (
        <>
            <h3>Calculadora de Total</h3>
            <input
                type="number"
                value={price}
                placeholder="Precio"
                onChange={(e) => setPrice(Number(e.target.value))}
            />
            <input
                type="number"
                value={qty}
                placeholder="Cantidad"
                onChange={(e) => setQty(Number(e.target.value))} // Fixed to setQty
            />
            
            <p>El total es: {total}</p>
        </>
    );
}

export default UseStateSuma;