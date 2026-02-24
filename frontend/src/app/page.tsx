'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { useAuth } from '../services/auth';

export default function HomePage() {
  const router = useRouter();
  const { isAuthenticated, loading } = useAuth();

  useEffect(() => {
    if (!loading && isAuthenticated) {
      router.push('/todos');
    }
  }, [isAuthenticated, loading, router]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <div className="w-6 h-6 border-3 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
      </div>
    );
  }

  if (isAuthenticated) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <nav className="navbar">
        <div className="px-4 mx-auto max-w-6xl sm:px-6">
          <div className="flex items-center justify-between h-14">
            <div className="flex items-center gap-2">
              <div className="w-5 h-5 bg-blue-600 rounded-lg flex items-center justify-center">
                <svg className="w-2.5 h-2.5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span className="text-sm font-semibold text-gray-900">TodoFlow</span>
            </div>
            <div className="flex items-center gap-3">
              <Link
                href="/auth/sign-in"
                className="text-xs font-medium text-gray-600 hover:text-gray-900 transition-colors"
              >
                Sign in
              </Link>
              <Link
                href="/auth/sign-up"
                className="btn-primary"
              >
                Get started
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <main>
        <div className="px-4 mx-auto max-w-3xl sm:px-6">
          <div className="flex flex-col items-center text-center pt-10 pb-8">

            {/* Badge */}
            <div className="inline-flex items-center gap-2 px-2.5 py-0.5 text-[0.6rem] font-medium text-blue-700 bg-blue-50 rounded-full border border-blue-200 mb-4">
              <span className="w-1.5 h-1.5 bg-blue-600 rounded-full animate-pulse"></span>
              Simple & Powerful
            </div>

            {/* Main Heading */}
            <h1 className="text-base sm:text-lg font-semibold text-gray-900 tracking-tight mb-2.5">
              Organize your tasks,
              <br />
              <span className="text-blue-600">achieve your goals</span>
            </h1>

            {/* Subtitle */}
            <p className="text-[0.6rem] text-gray-600 max-w-md mb-6">
              A beautiful and intuitive todo app that helps you stay focused and get things done
            </p>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-2.5 mb-8">
              <Link
                href="/auth/sign-up"
                className="btn-primary px-4 py-2"
              >
                Get started for free
              </Link>
              <Link
                href="/auth/sign-in"
                className="btn-secondary px-4 py-2"
              >
                Sign in
              </Link>
            </div>

            {/* Features */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 w-full max-w-2xl mt-6">
              <div className="p-3 card">
                <div className="w-5 h-5 bg-blue-100 rounded-lg flex items-center justify-center mb-1.5">
                  <svg className="w-2.5 h-2.5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <h3 className="text-[0.6rem] font-medium text-gray-900 mb-0.5">Lightning fast</h3>
                <p className="text-[0.5rem] text-gray-600">Quick and responsive interface</p>
              </div>

              <div className="p-3 card">
                <div className="w-5 h-5 bg-green-100 rounded-lg flex items-center justify-center mb-1.5">
                  <svg className="w-2.5 h-2.5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <h3 className="text-[0.6rem] font-medium text-gray-900 mb-0.5">Easy to use</h3>
                <p className="text-[0.5rem] text-gray-600">Clean and intuitive design</p>
              </div>

              <div className="p-3 card">
                <div className="w-5 h-5 bg-purple-100 rounded-lg flex items-center justify-center mb-1.5">
                  <svg className="w-2.5 h-2.5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <h3 className="text-[0.6rem] font-medium text-gray-900 mb-0.5">Secure</h3>
                <p className="text-[0.5rem] text-gray-600">Your data is safe with us</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}