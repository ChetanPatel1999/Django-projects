import React, { useState } from 'react'
import { useEffect } from 'react'
const App = () => {
  const [name, setName] = useState("")
  const [age, setAge] = useState(null)
  useEffect(() => {
    fetch('http://127.0.0.1:8000/store/home/')
      .then((response) => response.json())
      .then((data) => {
        setName(data.name)
        setAge(data.age)
      })
  }, [])
  return (
    <div>
      <h1>name : {name}</h1>
      <h1>age: {age}</h1>
    </div>
  )
}

export default App
