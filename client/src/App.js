import './App.css';
import ImageCpn from './Components/ImageCpn.js';
import SelectForm from './Components/SelectForm.js';
import ReactDOM from 'react-dom';

function App() {
  
  return (
    <div className="App">

      <div className="Input">
        <div className="Image">
          <ImageCpn />
        </div>

        <div className="Image_processing">
          <SelectForm />
        </div>
      </div>

      <div className="result hidden_result">

        <div className="Image_processed">
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
  );
}

export default App;
