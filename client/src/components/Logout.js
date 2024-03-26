import React from 'react';

const Logout = () => {
  const handleLogout = () => {
    // Implement logout logic here
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <button
        onClick={handleLogout}
        className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Logout
      </button>
    </div>
  );
};

export default Logout;
