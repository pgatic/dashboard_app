import { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
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

      {/* KPI cards */}
      <div style={{ display: "flex", gap: 20, marginBottom: 40 }}>
        {[
          { label: "Users", value: stats.users },
          { label: "Sales", value: stats.sales },
          { label: "Revenue", value: `$${stats.revenue}` },
        ].map((item) => (
          <div
            key={item.label}
            style={{
              flex: 1,
              padding: 20,
              borderRadius: 12,
              background: "#f3f4f6",
              textAlign: "center",
            }}
          >
            <h3>{item.label}</h3>
            <p style={{ fontSize: 24, fontWeight: "bold" }}>{item.value}</p>
          </div>
        ))}
      </div>

      {/* charts */}
      <div style={{ display: "flex", gap: 40 }}>
        <div style={{ flex: 1, height: 300 }}>
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

        <div style={{ flex: 1, height: 300 }}>
          <ResponsiveContainer>
            <BarChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="day" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="sales" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

export default App;
