/** @type {import('next').NextConfig} */
// --- START CRITICAL MODIFICATION ---
// Import dotenv and fs for ES Module compatibility
import dotenv from 'dotenv';
import path from 'path'; // Node.js path module
import fs from 'fs';     // Node.js file system module
import { fileURLToPath } from 'url'; // For __dirname equivalent in ESM

// Get current directory equivalent in ES Modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load .env.production
const envPath = path.resolve(__dirname, '.env.production');
if (fs.existsSync(envPath)) {
  dotenv.config({ path: envPath });
}
// --- END CRITICAL MODIFICATION ---

const nextConfig = {
    output: 'standalone',

    // No 'env' block here. `dotenv.config()` will populate process.env
    // which Next.js will then read for public variables implicitly.

    async rewrites() {
      return [
        {
          source: '/api/v1/:path*',
          destination: `${process.env.BACKEND_API_URL}/api/v1/:path*`, // Expects BACKEND_API_URL to be set
        },
      ];
    },
};
export default nextConfig;