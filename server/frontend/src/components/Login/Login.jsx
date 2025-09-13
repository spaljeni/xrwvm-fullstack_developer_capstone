import React, { useState } from "react";

export default function Login() {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");

  const submit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(window.location.origin + "/djangoapp/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ userName, password }),
      });
      const json = await res.json();
      if (json.status === "Authenticated") {
        sessionStorage.setItem("username", json.userName);
        window.location.href = window.location.origin; // na home
      } else {
        alert("Login failed (provjeri user/pass ili kreiraj korisnika u adminu).");
      }
    } catch (err) {
      alert("Greška pri loginu: " + err);
    }
  };

  return (
    <div style={{maxWidth: 420, margin: "40px auto", padding: 24, border: "1px solid #ddd", borderRadius: 12}}>
      <h2 style={{marginBottom: 16}}>Login</h2>
      <form onSubmit={submit}>
        <div style={{marginBottom: 12}}>
          <label>Username</label>
          <input
            style={{width: "100%", padding: 8, marginTop: 6}}
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            placeholder="username"
            required
          />
        </div>
        <div style={{marginBottom: 16}}>
          <label>Password</label>
          <input
            style={{width: "100%", padding: 8, marginTop: 6}}
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="password"
            required
          />
        </div>
        <button type="submit" style={{padding: "10px 16px"}}>Sign in</button>
      </form>
    </div>
  );
}
