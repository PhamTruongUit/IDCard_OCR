import "./ImageCpn.css";
import React, { useState } from "react";
import MagicDropZone from "react-magic-dropzone";
// import upload_image from '../upload_image.png';
import upload_image from '../../img/pngwing.com.jpeg'


export default function ImageCpn() {
  const [image, setImage] = useState(upload_image);

  function onDrop(accepted, rejected, links) {
    setImage(accepted[0].preview || links[0]);
  }

  return (
    <div className="input_image">
      <MagicDropZone
        accept="image/jpeg, image/png, .jpg, .jpeg, .png"
        onDrop={onDrop}
        multiple={false}
        className="input"
      >
        <img
          alt=""
          src={image}
          className="image_place"
        />
      </MagicDropZone>
    </div>
  );
}