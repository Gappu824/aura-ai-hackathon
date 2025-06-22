# Stage 1: Dependency Installation & Build
FROM node:18 AS builder

WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# --- START CRITICAL MODIFICATION ---
# Copy .env.production into the build context for dotenv to pick up
COPY .env.production ./.env.production
# --- END CRITICAL MODIFICATION ---

# Install dependencies
RUN npm install

# Copy the rest of your application code
COPY . .

# Set NODE_ENV for production build
ENV NODE_ENV production

# Build the Next.js application
RUN npm run build

# Stage 2: Production Runtime
FROM node:18

WORKDIR /app

# Copy built artifacts
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# CRITICAL: Set the environment variable for runtime
# This value will be provided by App Runner during service creation.
ENV NEXT_PUBLIC_API_URL=__APP_RUNNER_API_URL_RUNTIME_PLACEHOLDER__ 

EXPOSE 3000

CMD ["npm", "run", "start"]