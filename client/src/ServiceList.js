import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const ServiceList = () => {
    const [services, setServices] = useState([]);

    useEffect(() => {
        // Fetch the list of services from the server
        fetch('/services')
            .then(response => response.json())
            .then(data => setServices(data))
            .catch(error => console.error('Error fetching services:', error));
    }, []);

    return (
        <div>
            <h2>Services</h2>
            <ul>
                {/* Map over the services array to render each service as a list item */}
                {services.map(service => (
                    <li key={service.id}>
                        {/* Link to the ServiceDetail component for each service */}
                        <Link to={`/services/${service.id}`}>{service.name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ServiceList;
