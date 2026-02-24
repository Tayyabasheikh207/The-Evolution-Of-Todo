// API client for todo operations

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

// Get authorization header with token
const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
  };
};

// Get all todos for the authenticated user
export const getTodos = async (): Promise<any[]> => {
  const response = await fetch(`${API_BASE_URL}/todos`, {
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to fetch todos');
  }

  const data = await response.json();
  return data.todos || data;
};

// Create a new todo
export const createTodo = async (todoData: { content: string; completed: boolean }): Promise<any> => {
  const response = await fetch(`${API_BASE_URL}/todos`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify(todoData),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to create todo');
  }

  return await response.json();
};

// Update a todo
export const updateTodo = async (id: string, updates: Partial<{ content: string; completed: boolean }>): Promise<any> => {
  const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
    method: 'PUT',
    headers: getAuthHeaders(),
    body: JSON.stringify(updates),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to update todo');
  }

  return await response.json();
};

// Toggle todo completion status
export const toggleTodoCompletion = async (id: string): Promise<any> => {
  const response = await fetch(`${API_BASE_URL}/todos/${id}/toggle-complete`, {
    method: 'PATCH',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to toggle todo completion');
  }

  return await response.json();
};

// Delete a todo
export const deleteTodo = async (id: string): Promise<void> => {
  const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
    method: 'DELETE',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to delete todo');
  }
};

// Sign up a new user
export const signUp = async (userData: { email: string; password: string }) => {
  const response = await fetch(`${API_BASE_URL}/auth/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || 'Signup failed');
  }

  return data;
};

// Sign in a user
export const signIn = async (credentials: { email: string; password: string }) => {
  const response = await fetch(`${API_BASE_URL}/auth/signin`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(credentials),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || 'Signin failed');
  }

  return data;
};

// Sign out a user
export const signOut = async () => {
  const response = await fetch(`${API_BASE_URL}/auth/signout`, {
    method: 'POST',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Signout failed');
  }

  return await response.json();
};