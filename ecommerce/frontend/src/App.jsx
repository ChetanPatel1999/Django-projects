import React, { useState } from 'react'
import { useEffect } from 'react'
const App = () => {
  const [products, setProducts] = useState([])
  useEffect(() => {
    fetch('http://127.0.0.1:8000/store/products')
      .then((response) => response.json())
      .then((data) => {
        console.log(data)
        setProducts(data)
      })
  }, [])
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Products List</h1>
      {products.map((product, idx) => (
        <div className="border bg-gray-200 border-gray-300 p-4 m-2" key={idx} >
          <h2 className="text-xl font-semibold">{product.name}</h2>
          <p className="text-gray-600">{product.description}</p>
          <p className="text-lg font-bold">{product.price}</p>
        </div>
      ))}
    </div>
  )
}

export default App
