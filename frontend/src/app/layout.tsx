import '../styles/globals.css';
import type { Metadata } from 'next';
import AppWrapper from '../components/AppWrapper';

export const metadata: Metadata = {
  title: 'TodoFlow - Modern Task Management',
  description: 'Organize your life with TodoFlow - A modern SaaS todo application',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
      </head>
      <body className="font-inter antialiased">
        <AppWrapper>{children}</AppWrapper>
      </body>
    </html>
  );
}