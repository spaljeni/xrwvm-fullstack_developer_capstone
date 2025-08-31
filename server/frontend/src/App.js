import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";

function App() {
  return (
    <Routes>
      {/* Login page */}
      <Route path="/login" element={<LoginPanel />} />

      {/* Register page */}
      <Route path="/register" element={<Register />} />

      {/* Po potrebi kasnije možeš dodati još ruta */}
    </Routes>
  );
}

export default App;
