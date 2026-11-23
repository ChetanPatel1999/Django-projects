import React, { useState } from 'react'
import ProductList from './pages/ProductList'
import { Routes, Route } from 'react-router-dom'
import ProductDetails from './pages/ProductDetails'
const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/product/:product_id" element={<ProductDetails />} />
      </Routes>
    </div>
  )
}

export default App
