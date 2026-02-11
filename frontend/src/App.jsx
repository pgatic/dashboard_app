import { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

function App() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/stats")
      .then((res) => res.json())
      .then((data) => setStats(data));
  }, []);

  if (!stats) return <div>Loading...</div>;

  // priprema podataka za recharts
  const chartData = stats.sales_history.map((value, index) => ({
    day: `D${index + 1}`,
    sales: value,
  }));

  return (
    <div style={{ padding: 40, fontFamily: "sans-serif" }}>
      <h1>Dashboard</h1>

      {/* KPI */}
      <div style={{ display: "flex", gap: 20, marginBottom: 40 }}>
        <div>Users: {stats.users}</div>
        <div>Sales: {stats.sales}</div>
        <div>Revenue: ${stats.revenue}</div>
      </div>

      {/* Line chart */}
      <div style={{ width: "100%", height: 300 }}>
        <ResponsiveContainer>
          <LineChart data={chartData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="day" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="sales" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default App;
