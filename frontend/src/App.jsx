import { useEffect, useState } from "react";

function App() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/stats")
      .then(res => res.json())
      .then(data => setStats(data));
  }, []);

  return (
    <div style={{ padding: 40 }}>
      <h1>Dashboard</h1>

      {!stats ? (
        <p>Loading...</p>
      ) : (
        <ul>
          <li>Users: {stats.users}</li>
          <li>Sales: {stats.sales}</li>
          <li>Orders: {stats.orders}</li>
        </ul>
      )}
    </div>
  );
}

export default App;
