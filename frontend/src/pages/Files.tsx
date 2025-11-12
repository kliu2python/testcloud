import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Files() {
  const [files, setFiles] = useState([])
  const [uploading, setUploading] = useState(false)

  useEffect(() => {
    axios.get("/api/files/list").then(res => setFiles(res.data.files))
  }, [])

  const upload = async (e: any) => {
    if (!e.target.files.length) return

    setUploading(true)

    const formData = new FormData()
    formData.append("file", e.target.files[0])

    await axios.post("/api/files/upload", formData)
    setUploading(false)

    const res = await axios.get("/api/files/list")
    setFiles(res.data.files)
  }

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Test Files</h2>

      <input type="file" onChange={upload} />

      {uploading && <p className="mt-2 text-blue-500">Uploading...</p>}

      <ul className="mt-4 list-disc pl-5">
        {files.map((f: any, idx) => <li key={idx}>{f}</li>)}
      </ul>
    </div>
  )
}
