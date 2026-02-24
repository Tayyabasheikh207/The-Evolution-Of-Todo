'use client';

import React from 'react';
import { AuthProvider } from '../services/auth';

export default function AppWrapper({ children }: { children: React.ReactNode }) {
  return (
    <AuthProvider>
      {children}
    </AuthProvider>
  );
}