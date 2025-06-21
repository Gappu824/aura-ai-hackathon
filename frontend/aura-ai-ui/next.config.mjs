/** @type {import('next').NextConfig} */
const nextConfig = {
    // Remove 'output: "export"' or set to default if present
    // output: 'standalone', // Optional: for smaller Docker image, but default is fine

    env: {
        // This variable will be picked up by Next.js at build time.
        // Replace with your ACTUAL API Gateway URL.
        NEXT_PUBLIC_API_URL: 'https://nm8a6zynv9.execute-api.us-east-1.amazonaws.com',
    },
    // Remove 'rewrites' here as they are not typically used with App Runner proxying directly to a separate API.
};
export default nextConfig;