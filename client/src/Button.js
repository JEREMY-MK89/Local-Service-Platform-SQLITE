import React from 'react';
import { Link } from 'react-router-dom';

const Button = ({ to, text }) => {
  return (
    <li className="mr-6">
      <Link to={to} className="text-white hover:text-gray-400">{text}</Link>
    </li>
  );
};

export default Button;
