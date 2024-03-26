import React from 'react';

const ServiceList = ({ services }) => {
  return (
    <div className="mt-8">
      <h2 className="text-2xl font-bold mb-4">Service List</h2>
      <ul>
        {services.map(service => (
          <li key={service.id} className="mb-2">
            <div className="p-4 border rounded shadow">
              <h3 className="font-bold text-lg">{service.name}</h3>
              <p className="text-gray-600">{service.category}</p>
              <p className="text-gray-600">Rating: {service.rating}</p>
              <p className="text-gray-600">Reviews: {service.reviews.length}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ServiceList;
