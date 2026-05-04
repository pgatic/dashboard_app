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
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    async function fetchStats() {
      setLoading(true);
      setError("");

      try {
        const res = await fetch(`${apiBaseUrl}/api/stats`);

        if (!res.ok) {
          throw new Error("Failed to load dashboard stats.");
        }

        const data = await res.json();
        setStats(data);
      } catch (err) {
        setError(err.message || "Failed to load dashboard stats.");
      } finally {
        setLoading(false);
      }
    }

    fetchStats();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;
  if (!stats) return null;

  // priprema podataka za recharts
  const chartData = stats.sales_history;

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <div className="max-w-6xl mx-auto space-y-10">
        <h1 className="text-3xl font-bold">Dashboard</h1>

        {/* KPI cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            { label: "Users", value: stats.users },
            { label: "Sales", value: stats.sales },
            { label: "Revenue", value: `$${stats.revenue}` },
          ].map((item) => (
            <div
              key={item.label}
              className="bg-white rounded-2xl shadow p-6 text-center"
            >
              <p className="text-gray-500 text-sm">{item.label}</p>
              <p className="text-2xl font-bold mt-2">{item.value}</p>
            </div>
          ))}
        </div>

        {/* Charts */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white rounded-2xl shadow p-6 h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="day" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="sales" />
              </LineChart>
            </ResponsiveContainer>
          </div>

          <div className="bg-white rounded-2xl shadow p-6 h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
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
    </div>
  );
}

export default App;
