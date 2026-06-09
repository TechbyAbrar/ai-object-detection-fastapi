const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const detectObjects = async (
  file,
  confidence
) => {
  const formData = new FormData();

  formData.append("file", file);

  const response = await fetch(
    `${API_BASE_URL}/api/v1/images/detect?confidence=${confidence}`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error("Detection failed");
  }

  return response.json();
};

export const getResultImageUrl = (
  downloadUrl
) => {
  return `${API_BASE_URL}${downloadUrl}`;
};