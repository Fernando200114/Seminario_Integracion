import React from "react";

type Props = {
    hours: number[];
    setHours: React.Dispatch<React.SetStateAction<number[]>>;
};

export default function WorkDays({ hours, setHours }: Props) {
    const days = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie'];

    const changeHour = (i: number, value: string) => {
        const hourValue = Number(value) || 0;
        setHours((prev) =>
            prev.map((v, idx) => (idx === i ? hourValue : v))
        );
    }; 

    return (
        <>
            <h3>Pregunta 1: WorkDays.tsx</h3>
            {days.map((d, i) => (
                <div key={d} style={{ marginBottom: "10px" }}>
                    <label>{d}: </label>
                    <input
                        min={0}
                        type="number"
                        value={hours[i]}
                        placeholder="Horas"
                       
                        onChange={(e) => changeHour(i, e.target.value)}
                    />
                </div>
            ))}
        </>
    );
}