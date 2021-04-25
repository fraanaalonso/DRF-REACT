import { useState } from "react"

//Recibe un objeto y manipulo sus propiedades modificando el estado
export const useForm = ( initialState = {}) => {
    const [values, setValues] = useState(initialState);

    const handleInputChange = ({ target }) => {
        setValues({
            ...values,
            [target.name]: target.value
        })
    }


    return {
        values, 
        handleInputChange
    }
}
