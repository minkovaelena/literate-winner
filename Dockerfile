FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]

# Update 2026-01-10 23:15

# Update 2025-12-30 18:52

# Update 2025-10-04 20:39

# Update 2026-01-24 20:01

# Update 2025-09-21 19:12
