import React, { useState } from 'react';
const Signup = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add signup message
        console.log('Signup Succesful!!');
    };

    return (
        <div>
            <h2>Signup</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Signup</button>
            </form>
        </div>
    );
};

// Login Component
const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add your login message
        console.log('Welcome!!');
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

// Logout Component
const Logout = () => {
    const handleLogout = () => {
        // Add your logout logic here
        console.log('Logout succesfully!');
    };

    return (
        <div>
            <h2>Logout</h2>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

// ReviewForm Component
const ReviewForm = () => {
    const [content, setContent] = useState('');
    const [rating, setRating] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add your review form submission logic here
        console.log('Review submitted!!');
    };

    return (
        <div>
            <h2>Create Review</h2>
            <form onSubmit={handleSubmit}>
                <textarea placeholder="Content" value={content} onChange={(e) => setContent(e.target.value)} />
                <input type="number" placeholder="Rating" value={rating} onChange={(e) => setRating(e.target.value)} />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export { Signup, Login, Logout, ReviewForm };
