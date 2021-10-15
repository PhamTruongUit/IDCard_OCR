import "./Image_processing.css";
import React from "react";
import FormControlLabel from '@mui/material/FormControlLabel';
import FormGroup from '@mui/material/FormGroup';
import PropTypes from "prop-types";
import { Checkbox } from "@mui/material";
import { createTheme, ThemeProvider } from '@mui/material/styles';

Image_processing.propTypes = {
    handleArray: PropTypes.func
  };

export default function Image_processing(props){

    const { handleArray } = props;
    const handleChange = (event) => {
        handleArray(event);
    };

    
    return (
        // <div className='Form_check_box hidden_form_check_box '>
        //     <div className="Form_check_box_item">
        //         <input type="checkbox" name="img_processing" value="1" id="img_processing-1" /> Threshold
        //     </div>
        //     <div className="Form_check_box_item">
        //         <input type="checkbox" name="img_processing" value="2" id="img_processing-2" /> Histogram Equalization
        //     </div>
        //     <div className="Form_check_box_item">
        //          <input type="checkbox" name="img_processing" value="3" id="img_processing-3" /> Increase Contrast
        //     </div>
        // </div>

        <div className='Form_check_box hidden_form_check_box '>
                <ThemeProvider theme={theme}>
                    <div className="Form_check_box_item">
                    <FormControlLabel
                        value="1" 
                        control={<Checkbox sx={{color: '#FF275D',}}/>}
                        label={<span style={{ fontSize: '15px' }}>Threshold</span>}
                        onChange={handleChange}
                        sx={{fontSize: 16,}}
                    />
                    </div>

                    <div className="Form_check_box_item">
                    <FormControlLabel
                        value="2" 
                        control={<Checkbox sx={{color: '#FF275D',}}/>}
                        label={<span style={{ fontSize: '15px' }}>Histogram Equalization</span>}
                        onChange={handleChange}
                        sx={{fontSize: 16,}}
                    />
                    </div>

                    <div className="Form_check_box_item">
                    <FormControlLabel
                        value="3" 
                        control={<Checkbox sx={{color: '#FF275D',}}/>}
                        label={<span style={{ fontSize: '15px' }}>Increase Contrast</span>}
                        onChange={handleChange}
                        sx={{fontSize: 16,}}                    
                    />
                    </div>  
                </ThemeProvider>
                
        </div>
    )
}


const theme = createTheme({
    palette: {
      primary: {
        main: '#FF275D',
  
      },
    },
  });