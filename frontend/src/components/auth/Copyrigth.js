import { Typography } from '@material-ui/core'
import React from 'react'

export const Copyrigth = () => {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
        {'Copyright © '}
            Economic Hub
        {" "}{new Date().getFullYear()}
        {'.'}
        </Typography>
    )
}
