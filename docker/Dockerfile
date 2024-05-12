# Builder Stage
FROM node:14 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Production Stage
FROM node:14-alpine
WORKDIR /app
COPY --from=builder /app ./
EXPOSE 3000
CMD ["npm", "start"]

