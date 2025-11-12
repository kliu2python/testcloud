import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'

import Dashboard from './pages/Dashboard'
import Devices from './pages/Devices'
import Reports from './pages/Reports'
import Files from './pages/Files'

import './index.css'

function App() {
  return (
    <BrowserRouter>
      <div className="flex h-screen">
        <aside className="w-64 bg-gray-800 text-white p-4 flex flex-col">
          <h1 className="text-2xl font-bold mb-6">TestCloud</h1>
          <nav className="flex flex-col space-y-3">
            <Link to="/" className="hover:text-yellow-300">Dashboard</Link>
            <Link to="/devices" className="hover:text-yellow-300">Devices</Link>
            <Link to="/reports" className="hover:text-yellow-300">Reports</Link>
            <Link to="/files" className="hover:text-yellow-300">Files</Link>
          </nav>
        </aside>

        <main className="flex-1 overflow-y-auto p-6 bg-white">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/devices" element={<Devices />} />
            <Route path="/reports" element={<Reports />} />
            <Route path="/files" element={<Files />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
