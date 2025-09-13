import React, { useEffect, useState } from "react";

export default function Dealers() {
  const username = sessionStorage.getItem("username") || "";
  const [dealers, setDealers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState("");

  useEffect(() => {
    const load = async () => {
      try {
        const res = await fetch(window.location.origin + "/djangoapp/dealers");
        if (!res.ok) throw new Error("HTTP " + res.status);
        const json = await res.json();
        setDealers(json.dealers || []);
      } catch (e) {
        setErr(String(e));
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  return (
    <div style={{ maxWidth: 960, margin: "40px auto", padding: 24 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
        <h2 style={{ margin: 0 }}>Dealerships</h2>
        <div style={{ color: "#666", fontSize: 14 }}>
          {username ? `Signed in as ${username}` : "Guest"}
        </div>
      </div>

      {loading && <p>Loading dealers…</p>}
      {err && <p style={{ color: "crimson" }}>Failed to load dealers: {err}</p>}

      {!loading && !err && (
        <div style={{ overflowX: "auto", border: "1px solid #eee", borderRadius: 12 }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "#fafafa" }}>
                <th style={{ textAlign: "left", padding: "12px 16px", borderBottom: "1px solid #eee" }}>#</th>
                <th style={{ textAlign: "left", padding: "12px 16px", borderBottom: "1px solid #eee" }}>Dealer</th>
                <th style={{ textAlign: "left", padding: "12px 16px", borderBottom: "1px solid #eee" }}>City</th>
                <th style={{ textAlign: "left", padding: "12px 16px", borderBottom: "1px solid #eee" }}>Phone</th>
              </tr>
            </thead>
            <tbody>
              {dealers.map((d) => (
                <tr key={d.id}>
                  <td style={{ padding: "10px 16px", borderBottom: "1px solid #f2f2f2" }}>{d.id}</td>
                  <td style={{ padding: "10px 16px", borderBottom: "1px solid #f2f2f2" }}>{d.name}</td>
                  <td style={{ padding: "10px 16px", borderBottom: "1px solid #f2f2f2" }}>{d.city}</td>
                  <td style={{ padding: "10px 16px", borderBottom: "1px solid #f2f2f2" }}>{d.phone}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
