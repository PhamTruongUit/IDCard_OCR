import React from 'react';
import PropTypes from 'prop-types';
import { Button } from "@mui/material";
import {makeStyles} from  '@mui/styles'
ButtonApply.propTypes = {
    onImageLoaded: PropTypes.func,
};
const useStyles = makeStyles({
  container:{
    textAlign: 'center',
  },
  btn:{
    border: 'none',
    margin: 20,
    width: 200,
    heigh: 50,
    fontSize: 20,
    borderRadius: 6,
    textTransform: 'uppercase',
    boxShadow: '0 3px 5px 2px rgba(255, 105,135, 0.3)',
    cursor: 'pointer',
    color: '#fff',
    backgroundImage: 'linear-gradient(to right top, #f0a44c, #ff877d, #f77fb9, #b78fe5, #4e9eec)',
    backgroundSize: '200%',
    transition: '0.4s',
    '&:hover':{
      backgroundPosition: 'right',
    },
  }
})

function ButtonApply(props) {
    const {onImageLoaded} = props;
    const classes = useStyles();
    return (
        <div className={classes.container}>
        <Button 
          className={`${classes.btn}`} 
          onClick={onImageLoaded}
        >
          APPLY
        </Button>
        </div>
    );
}

export default ButtonApply;