function ResultImage({
  title,
  image,
}) {
  if (!image) return null;

  return (
    <div className="image-card">
      <h3>{title}</h3>

      <img
        src={image}
        alt={title}
      />
    </div>
  );
}

export default ResultImage;