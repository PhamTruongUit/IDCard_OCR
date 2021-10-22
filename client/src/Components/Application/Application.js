
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
                  <SelectForm setProgress={setProgress}/>
              </div>
            </div>
            {/* Result */}
            <div className=" col-sm-12 col-md-12 col-lg-6 col-xl-6 result hidden_result "> {/*  */}

              <div className="image_processed">

                <img id="Image_processed"></img>
              </div>

              <div className="result_info">

                <div className="image_info">
                  <span className="title">Information of Passport</span>
                  <span id="content" className="content"></span>
                </div>

              </div>
            </div>


          </div>
        </div>

   </BrowserRouter>
  );
}

export default Application;