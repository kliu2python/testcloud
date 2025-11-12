import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Dashboard() {
  const [vms, setVms] = useState([])

  useEffect(() => {
    axios.get('/api/dashboard/vms').then(res => {
      setVms(res.data.vms)
    })
  }, [])

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">VM Dashboard</h2>

      <table className="min-w-full border">
        <thead className="bg-gray-100">
          <tr>
            <th className="px-3 py-2 border">Name</th>
            <th className="px-3 py-2 border">Platform</th>
            <th className="px-3 py-2 border">Version</th>
            <th className="px-3 py-2 border">Priority</th>
            <th className="px-3 py-2 border">Result</th>
            <th className="px-3 py-2 border">Failures</th>
          </tr>
        </thead>

        <tbody>
          {vms.map((vm: any, idx) => (
            <tr key={idx} className="text-center">
              <td className="px-3 py-2 border">{vm.name}</td>
              <td className="px-3 py-2 border">{vm.platform}</td>
              <td className="px-3 py-2 border">{vm.version}</td>
              <td className="px-3 py-2 border">{vm.priority}</td>
              <td className="px-3 py-2 border">{vm.result}</td>
              <td className="px-3 py-2 border">{vm.failures}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
