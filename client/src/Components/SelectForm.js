import react, { useState } from "react";
import Image_processing from "./Image_processing.js";
import App from "../App.js";
import axios from "axios";
import "./SelectForm.css";

export default function SelectForm() {
  const [myChose, setMyChose] = useState("auto");

  function handleChange(event) {
    setMyChose(event.target.value);
    if (event.target.value === "custom") {
      var element = document.getElementsByClassName("Form_check_box")[0];
      element.classList.remove("hidden_form_check_box");
      element.classList.add("flex");
    } else {
      var element = document.getElementsByClassName("Form_check_box")[0];
      element.classList.add("hidden_form_check_box");
      element.classList.remove("flex");
    }
  }

  function get_image() {
    const img = document.getElementsByClassName("Image_place")[0];
    return img;
  }

  function getBase64Image(img) {
    var canvas = document.createElement("canvas");
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
    var e_info = document.getElementById('content');
    e_info.innerText = '';
  }

  function displayResult(img, text){
    var e_image = document.getElementById('Image_processed')
    e_image.src = 'data:image/png;base64,' + img;

    var e_display = document.getElementsByClassName("result")[0];
    e_display.classList.remove("hidden_result");

    var e_info = document.getElementById('content');
    e_info.innerText = text;
  }

  function onImageLoaded() {
    removeResult()
    var img = get_image();
    var base64 = getBase64Image(img);

    var img_processing = get_process();

    var bodyFormData = new FormData();
    bodyFormData.append("img", base64);
    bodyFormData.append("lst", img_processing);

    axios({
      method: "post",
      url: "http://localhost:3000/app",
      data: bodyFormData,
    })
      .then(function (response) {
        var result = response["data"];
        img = result["image"];
        var text = result["text"];
        
        displayResult(img, text)
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  function get_process() {
    let values = [];
    if (myChose === "custom") {
      const checkboxes = document.querySelectorAll(
        `input[name="img_processing"]:checked`
      );
      if (checkboxes.length === 0) {
        values.push("none");
      } else {
        checkboxes.forEach((checkbox) => {
          values.push(checkbox.value);
        });
      }
    } else {
      values.push(myChose);
    }

    return values;
  }

  return (
    <div className="form_submit">
      <form>
        <select value={myChose} onChange={handleChange}>
          <option value="auto">auto</option>
          <option value="custom">custom</option>
          <option value="none">none</option>
        </select>
      </form>

      <Image_processing />

      <button onClick={onImageLoaded}>APPLY</button>
    </div>
  );
}
