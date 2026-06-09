import {
  useState,
} from "react";

import UploadCard from "../components/UploadCard";
import Loader from "../components/Loader";
import ResultImage from "../components/ResultImage";
import DetectionTable from "../components/DetectionTable";

import {
  detectObjects,
  getResultImageUrl,
} from "../api/detectionApi";

function Home() {
  const [file, setFile] =
    useState(null);

  const [confidence,
    setConfidence] =
    useState(0.25);

  const [loading,
    setLoading] =
    useState(false);

  const [detections,
    setDetections] =
    useState([]);

  const [originalImage,
    setOriginalImage] =
    useState("");

  const [resultImage,
    setResultImage] =
    useState("");

  const handleSubmit =
    async () => {
      try {
        setLoading(true);

        const data =
          await detectObjects(
            file,
            confidence
          );

        setDetections(
          data.detections
        );

        setOriginalImage(
          URL.createObjectURL(
            file
          )
        );

        setResultImage(
          getResultImageUrl(
            data.download_url
          )
        );
      } catch (error) {
        alert(error.message);
      } finally {
        setLoading(false);
      }
    };

  return (
    <>
      <UploadCard
        file={file}
        setFile={setFile}
        confidence={confidence}
        setConfidence={
          setConfidence
        }
        onSubmit={
          handleSubmit
        }
        loading={loading}
      />

      {loading && <Loader />}

      <div className="image-grid">
        <ResultImage
          title="Original"
          image={
            originalImage
          }
        />

        <ResultImage
          title="Detection Result"
          image={resultImage}
        />
      </div>

      <DetectionTable
        detections={
          detections
        }
      />
    </>
  );
}

export default Home;