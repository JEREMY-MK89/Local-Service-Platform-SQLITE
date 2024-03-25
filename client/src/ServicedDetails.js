import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const ServiceDetail = () => {
    const [service, setService] = useState({});
    const { id } = useParams();

    useEffect(() => {
        // Fetch details of the specific service based on its ID
        fetch(`/services/${id}`)
            .then(response => response.json())
            .then(data => setService(data))
            .catch(error => console.error('Error fetching service detail:', error));
    }, [id]);

    return (
        <div>
            <h2>Service Detail</h2>
            <p>Name: {service.name}</p>
            <p>Category: {service.category}</p>
            {/* Add additional details as needed */}
        </div>
    );
};

export default ServiceDetail;
