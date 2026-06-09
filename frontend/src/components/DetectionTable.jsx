function DetectionTable({
  detections,
}) {
  if (
    !detections ||
    detections.length === 0
  )
    return null;

  return (
    <div className="table-wrapper">
      <h2>Detected Objects</h2>

      <table>
        <thead>
          <tr>
            <th>Label</th>
            <th>Confidence</th>
            <th>Bounding Box</th>
          </tr>
        </thead>

        <tbody>
          {detections.map(
            (item, index) => (
              <tr key={index}>
                <td>{item.label}</td>
                <td>
                  {(
                    item.confidence *
                    100
                  ).toFixed(2)}
                  %
                </td>
                <td>
                  {item.bbox.join(
                    ", "
                  )}
                </td>
              </tr>
            )
          )}
        </tbody>
      </table>
    </div>
  );
}

export default DetectionTable;