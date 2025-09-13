import React, { useState } from "react";

export default function Register() {
  const [userName, setUserName]   = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName]   = useState("");
  const [email, setEmail]         = useState("");
  const [password, setPassword]   = useState("");

  const submit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(window.location.origin + "/djangoapp/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          userName, password, firstName, lastName, email
        }),
      });
      const json = await res.json();
      if (json.status === "Authenticated") {
        sessionStorage.setItem("username", json.userName);
        window.location.href = window.location.origin; // home
      } else if (json.error === "Already Registered") {
        alert("User already registered — pokušaj login.");
        window.location.href = window.location.origin + "/login/";
      } else {
        alert("Registracija nije uspjela.");
      }
    } catch (err) {
      alert("Greška pri registraciji: " + err);
    }
  };

  return (
    <div style={{maxWidth: 520, margin: "40px auto", padding: 24, border: "1px solid #ddd", borderRadius: 12}}>
      <h2 style={{marginBottom: 16}}>Register</h2>
      <form onSubmit={submit}>
        <div style={{display:"grid", gap:12}}>
          <div>
            <label>Username</label>
            <input style={{width:"100%", padding:8, marginTop:6}}
                   value={userName} onChange={e=>setUserName(e.target.value)} required />
          </div>
          <div>
            <label>First name</label>
            <input style={{width:"100%", padding:8, marginTop:6}}
                   value={firstName} onChange={e=>setFirstName(e.target.value)} required />
          </div>
          <div>
            <label>Last name</label>
            <input style={{width:"100%", padding:8, marginTop:6}}
                   value={lastName} onChange={e=>setLastName(e.target.value)} required />
          </div>
          <div>
            <label>Email</label>
            <input type="email" style={{width:"100%", padding:8, marginTop:6}}
                   value={email} onChange={e=>setEmail(e.target.value)} required />
          </div>
          <div>
            <label>Password</label>
            <input type="password" style={{width:"100%", padding:8, marginTop:6}}
                   value={password} onChange={e=>setPassword(e.target.value)} required />
          </div>
        </div>
        <div style={{marginTop:16}}>
          <button type="submit" style={{padding:"10px 16px"}}>Create account</button>
        </div>
      </form>
    </div>
  );
}
