import React, { useState } from 'react';

const ServiceForm = () => {
    const [name, setName] = useState('');
    const [category, setCategory] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/services', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, category }),
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Clear form fields after successful submission
                setName('');
                setCategory('');
            })
            .catch(error => {
                console.error('Error creating service:', error);
            });
    };

    return (
        <div>
            <h2>Create Service</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
                <input type="text" placeholder="Category" value={category} onChange={(e) => setCategory(e.target.value)} />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default ServiceForm;
