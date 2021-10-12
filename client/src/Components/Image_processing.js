import "./Image_processing.css";
import React from "react";
import axios from "axios";

export default function Image_processing(){

    return (
        <div className='Form_check_box hidden_form_check_box '>
            <div className="Form_check_box_item">
                <input type="checkbox" name="img_processing" value="1" id="img_processing-1" /> Threshold
            </div>
            <div className="Form_check_box_item">
                <input type="checkbox" name="img_processing" value="2" id="img_processing-2" /> Histogram Equalization
            </div>
            <div className="Form_check_box_item">
            <input type="checkbox" name="img_processing" value="3" id="img_processing-3" /> Increase Contrast
            </div>
        </div>
    )
}