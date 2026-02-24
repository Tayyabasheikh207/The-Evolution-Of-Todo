import { useState } from 'react';

interface TodoFormProps {
  onCreateTodo: (content: string) => void;
}

export default function TodoForm({ onCreateTodo: onSubmit }: TodoFormProps) {
  const [content, setContent] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (content.trim()) {
      onSubmit(content.trim());
      setContent('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex gap-2">
      <input
        type="text"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="What needs to be done?"
        className="input-field text-body flex-1"
        maxLength={500}
        autoFocus
      />
      <button
        type="submit"
        disabled={!content.trim()}
        className="px-2.5 py-1.5 text-caption font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        Add
      </button>
    </form>
  );
}