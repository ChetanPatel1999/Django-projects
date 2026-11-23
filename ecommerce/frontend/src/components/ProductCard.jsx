import React from 'react'
import { Link } from 'react-router-dom'

const ProductCard = ({ product }) => {
    const apiUrl = import.meta.env.VITE_API_URL
    return (
        <Link to={`/product/${product.id}`}>
            <div className="bg-white cursor-pointer hover:-translate-y-1 duration-300 hover:shadow-lg transition-all  shadow-md rounded-lg overflow-hidden">
                <img src={`${apiUrl}${product.image}`} alt={product.name} className="w-full h-48 object-cover" />
                <h2 className="text-xl font-bold m-4">{product.name}</h2>
                <p className="text-lg text-green-600 font-semibold m-4">${product.price}</p>
            </div>
        </Link>
    )
}

export default ProductCard
