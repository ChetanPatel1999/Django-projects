import React from 'react'

const ProductCard = ({ product }) => {
    const apiUrl = import.meta.env.VITE_API_URL
    return (
        <div className="bg-white cursor-pointer hover:-translate-y-1 duration-300 hover:shadow-lg transition-all  shadow-md rounded-lg overflow-hidden">
            <img src={`${apiUrl}${product.image}`} alt={product.name} className="w-full h-48 object-cover" />
            <h2 className="text-xl font-bold m-4">{product.name}</h2>
            <p className="text-lg font-semibold m-4">${product.price}</p>
        </div>
    )
}

export default ProductCard
