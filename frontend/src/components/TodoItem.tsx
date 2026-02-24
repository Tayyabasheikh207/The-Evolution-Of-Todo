import { useState } from 'react';

interface Todo {
  id: string;
  content: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

interface TodoItemProps {
  todo: Todo;
  onToggleComplete: (id: string) => void;
  onUpdate: (id: string, updates: Partial<Todo>) => void;
  onDelete: (id: string) => void;
}

export default function TodoItem({ todo, onToggleComplete, onUpdate, onDelete }: TodoItemProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editContent, setEditContent] = useState(todo.content);

  const handleEdit = () => {
    setIsEditing(true);
    setEditContent(todo.content);
  };

  const handleSave = () => {
    if (editContent.trim()) {
      onUpdate(todo.id, { content: editContent.trim() });
      setIsEditing(false);
    }
  };

  const handleCancel = () => {
    setEditContent(todo.content);
    setIsEditing(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSave();
    } else if (e.key === 'Escape') {
      handleCancel();
    }
  };

  return (
    <li className="group py-2.5 px-3 border-b border-gray-100 last:border-0 hover:bg-gray-50 transition-colors">
      {isEditing ? (
        <div className="space-y-1.5">
          <input
            type="text"
            value={editContent}
            onChange={(e) => setEditContent(e.target.value)}
            onKeyDown={handleKeyDown}
            className="input-field text-body"
            autoFocus
            maxLength={500}
          />
          <div className="flex gap-1.5">
            <button
              onClick={handleSave}
              className="px-2 py-1 text-caption font-medium text-white bg-gray-900 rounded-md hover:bg-gray-800 transition-colors"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="px-2 py-1 text-caption font-medium text-gray-700 border border-gray-300 rounded-md hover:border-gray-400 transition-colors"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <div className="flex items-center justify-between">
          <div className="flex items-center flex-1 min-w-0">
            <input
              type="checkbox"
              checked={todo.completed}
              onChange={() => onToggleComplete(todo.id)}
              className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500 cursor-pointer"
            />
            <span className={`ml-2.5 text-body ${
              todo.completed ? 'line-through text-gray-500' : 'text-gray-900'
            }`}>
              {todo.content}
            </span>
          </div>

          <div className="flex items-center gap-1 ml-3 opacity-0 group-hover:opacity-100 transition-opacity">
            <button
              onClick={handleEdit}
              className="btn-icon"
              title="Edit"
            >
              <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
            </button>
            <button
              onClick={() => onDelete(todo.id)}
              className="btn-icon"
              title="Delete"
            >
              <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>
      )}
    </li>
  );
}