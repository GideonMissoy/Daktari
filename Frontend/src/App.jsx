import { useState } from 'react';
import Home from './pages/Landing/Home';
import VerifyEmail from './pages/Auth/VerifyEmail';
import Register from './pages/Auth/Register';
import Login from './pages/Auth/Login';
import ForgotPassword from './pages/Auth/ForgotPassword';

function Logout() {
  localStorage.clear();
  return <Navigate to='/login' />;
}

function RegisterAndLogout() {
  localStorage.clear();
  return <Register />;
}

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route exact path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/logout' element={<Logout />} />
          <Route path='/register' element={<RegisterAndLogout />} />
          <Route path='/reset-password' element={<ForgotPassword />} />
          <Route path='/verify-email' element={<VerifyEmail />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
