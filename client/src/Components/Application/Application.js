
import ImageCpn from '../ImageCpn/ImageCpn';
import SelectForm from '../SelectForm/SelectForm';
import React, { useEffect, useState } from "react";
import {BrowserRouter, Switch, Route, Link} from "react-router-dom";
import AOS from 'aos';
import 'aos/dist/aos.css';
import './Application.css'
AOS.init();
function Application() {
  const [progress, setProgress] = useState(false);
  const [result, setResult] = useState([]);
  // console.log(result);
  return (
   <BrowserRouter>    
        <div className=" container ">
          <div className="row field-input">
            {/* InPut */}
            <div data-aos="fade" data-aos-duration="2000" className="col-sm-12 col-md-12 col-lg-6 col-xl-6 input">
              <div className="image">
                  <ImageCpn progress={progress}/>
              </div>

              <div className="Image_processing">
                  <SelectForm setProgress={setProgress} setResult={setResult}/>
              </div>
            </div>
            {/* Result */}
            <div className=" col-sm-12 col-md-12 col-lg-6 col-xl-6 result hidden_result "> {/*  */}

              <div className="image_processed">

                <img alt="" id="Image_processed"></img>
              </div>

              <div className="result_info">

                <div className="image_info">
                  <span className="title">Text Recognize</span>
                  {Array.isArray(result) && result.map((value,index)=>{
                    return <p className="content" key={index}>{value}</p>
                  })}
                  {!Array.isArray(result) && <span className="content">{result}</span>}
                  
                </div>

              </div>
            </div>


          </div>
        </div>

   </BrowserRouter>
  );
}

export default Application;
