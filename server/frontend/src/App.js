import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/Login/Login";
import Register from "./components/Register/Register";
import Dealers from "./components/Dealers/Dealers";

export default function App() {
  return (
    <Routes>
      <Route path="/login/*" element={<Login />} />
      <Route path="/register/*" element={<Register />} />
      <Route path="/dealers/*" element={<Dealers />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
}
