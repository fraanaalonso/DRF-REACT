import { useState } from "react"

//Recibe un objeto y manipulo sus propiedades modificando el estado
export const useForm = ( initialState = {}) => {
    const [values, setValues] = useState(initialState);


    const reset = ( newFormState = initialState) => {
        setValues( newFormState );
    }
    const handleInputChange = ({ target }) => {
        setValues({
            ...values,
            [target.name]: target.value
        })
    }


    return [ values, handleInputChange, reset ];
}
