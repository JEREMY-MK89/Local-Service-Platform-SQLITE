import React, { useState } from 'react';

const ReviewForm = () => {
  const [rating, setRating] = useState('');
  const [comment, setComment] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Implement review submission logic here
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <h2 className="text-2xl font-bold mb-4">Write a Review</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Rating"
          value={rating}
          onChange={(e) => setRating(e.target.value)}
          min="1"
          max="5"
          className="block w-full mb-2 p-2 border rounded"
          required
        />
        <textarea
          placeholder="Comment"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          className="block w-full mb-2 p-2 border rounded"
          required
        ></textarea>
        <button
          type="submit"
          className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Submit Review
        </button>
      </form>
    </div>
  );
};

export default ReviewForm;
