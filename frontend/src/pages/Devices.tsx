import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Devices() {
  const [devices, setDevices] = useState([])

  useEffect(() => {
    axios.get('/api/devices/list').then(res => {
      const data = res.data.devices?.data || res.data.devices
      setDevices(data || [])
    })
  }, [])

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Available Devices</h2>

      <table className="min-w-full border">
        <thead className="bg-gray-100">
          <tr>
            <th className="px-3 py-2 border">Serial</th>
            <th className="px-3 py-2 border">Model</th>
            <th className="px-3 py-2 border">Status</th>
            <th className="px-3 py-2 border">Platform</th>
            <th className="px-3 py-2 border">Version</th>
          </tr>
        </thead>

        <tbody>
          {devices.map((dev: any, idx) => (
            <tr key={idx} className="text-center">
              <td className="px-3 py-2 border">{dev.serial}</td>
              <td className="px-3 py-2 border">{dev.model}</td>
              <td className="px-3 py-2 border">{dev.status}</td>
              <td className="px-3 py-2 border">{dev.platform}</td>
              <td className="px-3 py-2 border">{dev.version}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
