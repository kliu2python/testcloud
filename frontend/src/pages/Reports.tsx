import { useState } from 'react'
import axios from 'axios'

export default function Reports() {
  const [prompt, setPrompt] = useState("")
  const [result, setResult] = useState("")

  const analyze = async () => {
    const res = await axios.post("/api/ai/analyze", { prompt })
    const text = res.data?.choices?.[0]?.message?.content || JSON.stringify(res.data)
    setResult(text)
  }

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">AI Code Analysis</h2>

      <textarea
        className="border w-full p-2"
        rows={6}
        placeholder="Enter test code or description..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        className="mt-3 bg-blue-600 text-white px-4 py-2 rounded"
        onClick={analyze}
      >
        Analyze
      </button>

      {result && (
        <pre className="bg-gray-100 p-4 mt-4 whitespace-pre-wrap text-sm border">
          {result}
        </pre>
      )}
    </div>
  )
}
