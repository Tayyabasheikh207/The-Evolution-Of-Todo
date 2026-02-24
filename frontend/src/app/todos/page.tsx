'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '../../services/auth';
import { getTodos, createTodo, updateTodo, deleteTodo } from '../../services/api';
import TodoItem from '../../components/TodoItem';
import TodoForm from '../../components/TodoForm';

interface Todo {
  id: string;
  content: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
}

export default function TodosPage() {
  const { isAuthenticated, loading: authLoading, logout } = useAuth();
  const router = useRouter();
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    if (!authLoading && !isAuthenticated) {
      router.push('/auth/sign-in');
    } else if (isAuthenticated) {
      fetchTodos();
    }
  }, [isAuthenticated, authLoading, router]);

  const fetchTodos = async () => {
    try {
      setLoading(true);
      const data = await getTodos();
      setTodos(data);
      setError('');
    } catch (err: any) {
      setError(err.message || 'Failed to load todos');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTodo = async (content: string) => {
    try {
      const newTodo = await createTodo({ content, completed: false });
      setTodos([newTodo, ...todos]);
      setShowForm(false);
    } catch (err: any) {
      setError(err.message || 'Failed to create todo');
    }
  };

  const handleUpdateTodo = async (id: string, updates: Partial<Todo>) => {
    try {
      const updatedTodo = await updateTodo(id, updates);
      setTodos(todos.map(todo => todo.id === id ? updatedTodo : todo));
    } catch (err: any) {
      setError(err.message || 'Failed to update todo');
    }
  };

  const handleDeleteTodo = async (id: string) => {
    try {
      await deleteTodo(id);
      setTodos(todos.filter(todo => todo.id !== id));
    } catch (err: any) {
      setError(err.message || 'Failed to delete todo');
    }
  };

  const handleToggleComplete = async (id: string) => {
    try {
      const todo = todos.find(t => t.id === id);
      if (todo) {
        const updatedTodo = await updateTodo(id, { completed: !todo.completed });
        setTodos(todos.map(todo => todo.id === id ? updatedTodo : todo));
      }
    } catch (err: any) {
      setError(err.message || 'Failed to update todo');
    }
  };

  if (authLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <div className="text-center">
          <div className="w-6 h-6 mx-auto border-3 border-indigo-200 border-t-indigo-600 rounded-full animate-spin"></div>
          <p className="mt-3 text-caption text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <nav className="navbar">
        <div className="px-4 mx-auto max-w-5xl sm:px-6">
          <div className="flex items-center justify-between h-14">
            <div className="flex items-center gap-2">
              <div className="w-5 h-5 bg-blue-600 rounded-lg flex items-center justify-center">
                <svg className="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span className="text-sm font-semibold text-gray-900">TodoFlow</span>
            </div>
            <button
              onClick={logout}
              className="text-xs font-medium text-gray-600 hover:text-gray-900 transition-colors"
            >
              Sign out
            </button>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="dashboard-container">
        {/* Header */}
        <div className="mb-4">
          <h1 className="text-display text-gray-900">My Tasks</h1>
          <p className="mt-1 text-caption text-gray-600">{todos.length} {todos.length === 1 ? 'task' : 'tasks'}</p>
        </div>

        {/* Create Task Form */}
        {showForm && (
          <div className="mb-4 card p-3">
            <TodoForm onCreateTodo={handleCreateTodo} />
            <button
              onClick={() => setShowForm(false)}
              className="mt-2 text-caption text-gray-600 hover:text-gray-900"
            >
              Cancel
            </button>
          </div>
        )}

        {!showForm && (
          <button
            onClick={() => setShowForm(true)}
            className="mb-4 btn-outline px-3 py-1.5"
          >
            + New task
          </button>
        )}

        {/* Error Message */}
        {error && (
          <div className="p-2.5 mb-4 text-caption text-red-600 bg-red-50 border border-red-200 rounded-md">
            {error}
          </div>
        )}

        {/* Tasks List */}
        <div className="card">
          {loading ? (
            <div className="flex flex-col items-center justify-center py-12">
              <div className="w-5 h-5 border-3 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
              <p className="mt-3 text-caption text-gray-600">Loading...</p>
            </div>
          ) : todos.length === 0 ? (
            <div className="py-12 text-center">
              <div className="w-10 h-10 mx-auto mb-3 bg-gray-100 rounded-full flex items-center justify-center">
                <svg className="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                </svg>
              </div>
              <p className="text-gray-600 mb-3 text-body">No tasks yet</p>
              <button
                onClick={() => setShowForm(true)}
                className="text-caption text-blue-600 hover:text-blue-700 font-medium"
              >
                Create your first task
              </button>
            </div>
          ) : (
            <ul className="divide-y divide-gray-100">
              {todos.map(todo => (
                <TodoItem
                  key={todo.id}
                  todo={todo}
                  onToggleComplete={handleToggleComplete}
                  onUpdate={handleUpdateTodo}
                  onDelete={handleDeleteTodo}
                />
              ))}
            </ul>
          )}
        </div>
      </main>
    </div>
  );
}