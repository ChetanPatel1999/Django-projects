import React from 'react'
import { useState } from 'react'
import { useEffect } from 'react'
import ProductCard from '../components/ProductCard'

const ProductList = () => {
    const [products, setProducts] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const apiUrl = import.meta.env.VITE_API_URL
    useEffect(() => {
        fetch(`${apiUrl}/store/products/`)
            .then(response => response.json())
            .then(data => {
                setProducts(data)
                setLoading(false)
            })
            .catch(error => {
                setError(error)
                setLoading(false)
            })
    }, [])

    if (loading) {
        return <div className="flex flex-col items-center justify-center h-screen gap-4">
            <div className=" w-40 h-40 border-12 rounded-full border-gray-200 border-t-black animate-spin"></div>
            <p className="font-bold">Loading...</p>
        </div>
    }

    if (error) {
        return <div className="text-center text-red-500">Error: {error.message}</div>
    }

    return (
        <div className="w-full h-screen">
            <h1 className="text-2xl font-bold mb-4 text-center shadow-lg py-4">Product List</h1>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-4">
                {products.map(product => (
                    <ProductCard key={product.id} product={product} />
                ))}
            </div >
        </div >
    )
}

export default ProductList
