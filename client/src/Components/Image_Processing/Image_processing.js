import "./Image_processing.css";
import React from "react";
import FormControlLabel from '@mui/material/FormControlLabel';
import FormGroup from '@mui/material/FormGroup';
import PropTypes from "prop-types";
import { Checkbox } from "@mui/material";

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
                <div className="Form_check_box_item">
                <FormControlLabel
                    value="1" 
                    control={<Checkbox/>}
                    label={<span style={{ fontSize: '15px' }}>Threshold</span>}
                    onChange={handleChange}
                    sx={{fontSize: 16,}}
                    
                />
                </div>

                <div className="Form_check_box_item">
                <FormControlLabel
                    value="2" 
                    control={<Checkbox/>}
                    label={<span style={{ fontSize: '15px' }}>Histogram Equalization</span>}
                    onChange={handleChange}
                    sx={{fontSize: 11,}}
                />
                </div>

                <div className="Form_check_box_item">
                <FormControlLabel
                    value="3" 
                    control={<Checkbox/>}
                    label={<span style={{ fontSize: '15px' }}>Increase Contrast</span>}
                    onChange={handleChange}
                    sx={{fontSize: 16,}}                    
                />
                </div>
        </div>
    )
}