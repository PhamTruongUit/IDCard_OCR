import "./Image_processing.css";
import React from "react";
import FormControlLabel from "@mui/material/FormControlLabel";
import FormGroup from "@mui/material/FormGroup";
import PropTypes from "prop-types";
import { Checkbox } from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";

Image_processing.propTypes = {
  handleArray: PropTypes.func,
};

export default function Image_processing(props) {
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

    <div className="Form_check_box hidden_form_check_box ">
      <ThemeProvider theme={theme}>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="01"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Detect Object</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>

        <div className="Form_check_box_item">
          <FormControlLabel
            value="02"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={
              <span style={{ fontSize: "15px" }}>Histogram Equalization</span>
            }
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>

        <div className="Form_check_box_item">
          <FormControlLabel
            value="03"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={
              <span style={{ fontSize: "15px" }}>Increase Brightness</span>
            }
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="04"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={
              <span style={{ fontSize: "15px" }}>Decrease Brightness</span>
            }
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="05"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Increase Contract</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="06"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Decrease Contract</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="07"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Erosion</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="08"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Dilation</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="09"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Opening</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="10"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Closing</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="11"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Blur Median</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
        <div className="Form_check_box_item">
          <FormControlLabel
            value="12"
            control={<Checkbox sx={{ color: "#FF275D" }} />}
            label={<span style={{ fontSize: "15px" }}>Blur Bilateral</span>}
            onChange={handleChange}
            sx={{ fontSize: 16 }}
          />
        </div>
      </ThemeProvider>
    </div>
  );
}

const theme = createTheme({
  palette: {
    primary: {
      main: "#FF275D",
    },
  },
});
