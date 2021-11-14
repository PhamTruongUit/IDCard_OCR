import './App.css';
import HeaderNavBar from './Components/Header/HeaderNavBar.js';
// import ImageCpn from './Components/ImageCpn/ImageCpn.js';
// import ProgressBars from './Components/Progress/ProgressBars';
// import SelectForm from './Components/SelectForm/SelectForm.js';
import Information from './Components/Information/Information';
import NotFound from './Components/NotFound/NotFound'
import React, {useState } from "react";
import {BrowserRouter, Switch, Route, Link} from "react-router-dom";
import Application from './Components/Application/Application';
function App() {
  const [progress, setProgress] = useState(false);
  function handleProgress(){
    // console.log("hello app ne");
    if(progress === false){
      setProgress(true);
    }else(setProgress(false));
    console.log(progress);
  }
  
  return (
   <BrowserRouter>
     <div className="App background-img-1">
        <HeaderNavBar/>
        <Switch>
          <Route exact path="/">
            <Application/>    
          </Route>
          <Route path="/App">
            <Application/>
          </Route>
          <Route path="/Information">
            <Information/>
          </Route>
          <Route>
            <NotFound/>
          </Route>
        </Switch>




        {/* <div className=" container ">
          <div className="row field-input"> */}
            {/* InPut */}
            {/* <div className="col-sm-12 col-md-12 col-lg-6 col-xl-6 input">
              <div className="image">
                  <ImageCpn progress={progress}/>
              </div>

              <div className="Image_processing">
                  <SelectForm setProgress={setProgress}/>
              </div>
            </div> */}
            {/* Result */}
            {/* <div className=" col-sm-12 col-md-12 col-lg-6 col-xl-6 result hidden_result ">  */}

              {/* <div className="image_processed">

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
        */}
    </div>

   </BrowserRouter>
  );
}

export default App;
