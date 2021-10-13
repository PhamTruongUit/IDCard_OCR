import './App.css';
import HeaderNavBar from './Components/Header/HeaderNavBar.js';
import ImageCpn from './Components/ImageCpn/ImageCpn.js';
import SelectForm from './Components/SelectForm/SelectForm.js';

function App() {
  
  return (
    <div className="App background-img-1">
        <HeaderNavBar/>
      <div className="background-img">
        <div className=" container ">
          <div className="row field-input">
            {/* InPut */}
            <div className="col-sm-12 col-md-12 col-lg-6 col-xl-6 input">
              <div className="image">
                  <ImageCpn />
              </div>

              <div className="Image_processing">
                  <SelectForm />
              </div>
            </div>
            {/* Result */}
            <div className=" col-sm-12 col-md-12 col-lg-6 col-xl-6 result"> {/* hidden_result*/}

              <div className="image_processed">
                <img id="Image_processed"></img>
              </div>

              <div className="result_info">

                <div className="image_info">
                  <span className="title">Thông tin từ giấy tờ</span>
                  <span id="content" className="content"></span>
                </div>

              </div>
            </div>


          </div>
        </div>
      </div>
      
    </div>

  );
}

export default App;
