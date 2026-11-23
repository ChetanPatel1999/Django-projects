import React from 'react'
import { useState } from 'react'
import { useEffect } from 'react'
import { Link, useParams } from 'react-router-dom'
import { FaCartPlus } from "react-icons/fa";
import { FaArrowLeft } from "react-icons/fa6";

const ProductDetails = () => {
    const { product_id } = useParams()
    const [product, setproduct] = useState(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const apiUrl = import.meta.env.VITE_API_URL
    useEffect(() => {
        fetch(`${apiUrl}/store/product/${product_id}/`)
            .then(response => response.json())
            .then(data => {
                setproduct(data)
                setLoading(false)
            })
            .catch(err => {
                setError(err)
                setLoading(false)
            })
    }, [product_id])

    if (loading) return <div className="flex flex-col items-center justify-center h-screen gap-4">
        <div className=" w-40 h-40 border-12 rounded-full border-gray-200 border-t-black animate-spin"></div>
        <p className="font-bold">Loading...</p>
    </div>
    if (error) return <div>Error: {error.message}</div>
    if (!product) return <div>Product not found</div>

    return (
        <div className="w-full h-screen bg-gray-200 flex items-center justify-center">
            <div className="w-1/2  bg-white shadow-md flex gap-4 rounded-lg overflow-hidden">
                <div className="w-1/2 p-4">
                    <img src={`${apiUrl}${product.image}`} alt={product.name} className="w-full rounded-lg h-full object-cover" />
                </div>
                <div className="w-1/2 p-4 ">
                    <h1 className="text-3xl font-bold m-4">{product.name}</h1>
                    <p className="text-gray-700 font-medium text-sm m-4">{product.description}</p>
                    <p className="text-lg text-green-600 font-semibold m-4">${product.price}</p>
                    <button className="bg-blue-600 text-white px-4 mb-2 py-2 rounded hover:bg-blue-700 font-medium active:scale-95 cursor-pointer transition-all flex items-center gap-2">Add to Cart   <FaCartPlus /></button>
                    <Link to="/" className="font-medium text-blue-700  cursor-pointer flex items-center gap-2 "><FaArrowLeft />Back to Products</Link>
                </div>
            </div>
        </div>
    )
}

export default ProductDetails
