import { ToggleButton, ToggleButtonGroup } from "@mui/material";
import axios from "axios";
import { useState } from "react";
import ButtonApply from "../Button/ButtonApply.js";
import ImageProcessing from "../Image_Processing/Image_processing.js";
import "./SelectForm.css";
import "./ToggleButton.css"
import { createTheme, ThemeProvider } from '@mui/material/styles';
import PropTypes from "prop-types";

SelectForm.propTypes ={
  handleProgress: PropTypes.func,
  setProgress: PropTypes.func,
  setResult: PropTypes.func,
}

export default function SelectForm(props) {
  const { handleProgress, setProgress, setResult } = props;
  const [myChose, setMyChose] = useState("auto");
  const [option, setOption] = useState([]);
  const [buttonToggle, setButtonToggle] = useState(false);
  // const classes = useStyles();
  function handleChange(event) {
    setMyChose(event.target.value);
    // console.log(event.target.value);
    if (event.target.value === "custom") {
      let element = document.getElementsByClassName("Form_check_box")[0];
      element.classList.remove("hidden_form_check_box");
      element.classList.add("flex");
    } else {
      let element = document.getElementsByClassName("Form_check_box")[0];
      element.classList.add("hidden_form_check_box");
      element.classList.remove("flex");
    }
  }

  function get_image() {
    const img = document.getElementsByClassName("image_place")[0];
    
    return img;
  }

  function getBase64Image(img) {
    var canvas = document.createElement("canvas");
    // console.log(img)
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    var dataURL = canvas.toDataURL("image/png");
    return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
  }

  function removeResult(){
    var e_image = document.getElementById('Image_processed')
    e_image.removeAttribute('src');
    // var e_info = document.getElementById('content');
    // e_info.innerText = '';
    setResult([])
    var e_display = document.getElementsByClassName("result")[0];
    e_display.classList.add("hidden_result");
  }

  function displayResult(img, text){
    var e_image = document.getElementById('Image_processed')
    e_image.src = 'data:image/png;base64,' + img;
    var e_display = document.getElementsByClassName("result")[0];
    e_display.classList.remove("hidden_result");
    setProgress(false);
    setResult(text);
    // var e_info = document.getElementById('content');
    // e_info.innerText = text;
  }

  function onImageLoaded() {
    removeResult()
    // setButtonToggle(true);
    var img = get_image();
    console.log(img)
    var base64 = getBase64Image(img);
    var img_processing = get_process();
    var bodyFormData = new FormData();
    bodyFormData.append("img", base64);
    bodyFormData.append("lst", img_processing);
    // handleCheckProgress();
    setProgress(true);
    // Check
    // for (var value of bodyFormData.values()) {
    //   console.log(value);
    // }
    //--------------------
    axios({
      method: "post",
      url: "http://b7d6-1-55-220-244.ngrok.io/app", //http://localhost:3000/app
      data: bodyFormData,
    })
      .then(function (response) {
        var result = response["data"];
        img = result["image"];
        var text = result["text"];      
        displayResult(img, text);
        setButtonToggle(false);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  // LẤY OPTION
  function get_process() {
    let values = [];
    if (myChose === "custom") {
      // const checkboxes = document.querySelectorAll(
      //   `input[name="img_processing"]:checked`
      // );
      if (option.length === 0) {
        values.push("none");
      } else {
        // option.forEach((checkbox) => {
        //   values.push(checkbox.value);
        // });
        values = [...option];
      }
    } else {
      values.push(myChose);
    }
    console.log(values);
    values = JSON.stringify(values);
    return values;
  }


  // HANDLE CHECKBOX
  function handleCheckBox(event){
    if(event.target.checked === true){
      let newOptions = [...option];
      newOptions.push(event.target.value);
      setOption(newOptions);
    }else{
      let newOptions = [...option];
      const indexDelete = newOptions.indexOf(event.target.value);
      newOptions.splice(indexDelete,1);
      setOption(newOptions);
    }
    // console.log(option);
  }

  function handleCheckProgress(){
    handleProgress();
  }
  return (
    <div className="form_submit">
      {/* <form>
        <select value={myChose} onChange={handleChange}>
          <option value="auto">auto</option>
          <option value="custom">custom</option>
          <option value="none">none</option>
        </select>
      </form> */}
      <div className="form-controller">
        <ThemeProvider theme={theme}>
          
          <ToggleButtonGroup
            value={myChose}
            color="secondary"
            // exclusive
            onChange={handleChange}
          >
            <ToggleButton value="auto" >Auto</ToggleButton>
            <ToggleButton value="custom">Custom</ToggleButton>
            <ToggleButton value="none">None</ToggleButton>
            
          </ToggleButtonGroup>
        </ThemeProvider>
        
      </div>
      

      <ImageProcessing handleArray={handleCheckBox} />

      {/* <button onClick={onImageLoaded}>APPLY</button> */}

      <ButtonApply onImageLoaded={onImageLoaded} buttonToggle={buttonToggle} setButtonToggle={setButtonToggle}/>
    </div>
  );
}

const theme = createTheme({
  palette: {
    primary: {
      main: '#cccccc',

    },
    secondary: {
      
      main: '#FF275D',
      contrastText: '#ccc'
    },
  },
  typography: {
    fontFamily: [
      'Poppins',
      'sans-serif',
    ].join(','),
  },
});

