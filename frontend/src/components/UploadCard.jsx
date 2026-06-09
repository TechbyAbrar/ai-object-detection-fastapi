function UploadCard({
  file,
  setFile,
  confidence,
  setConfidence,
  onSubmit,
  loading,
}) {
  const handleChange = (e) => {
    if (e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  return (
    <div className="card">

      <h2>Upload Image</h2>

      <input
        type="file"
        accept="image/*"
        onChange={handleChange}
      />

      <div className="slider-container">
        <label>
          Confidence:
          {confidence}
        </label>

        <input
          type="range"
          min="0"
          max="1"
          step="0.05"
          value={confidence}
          onChange={(e) =>
            setConfidence(
              e.target.value
            )
          }
        />
      </div>

      <button
        disabled={!file || loading}
        onClick={onSubmit}
      >
        Detect Objects
      </button>
    </div>
  );
}

export default UploadCard;