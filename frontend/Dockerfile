FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json* ./

RUN npm install && \
    npm install -D @vitejs/plugin-react @tailwindcss/postcss tailwindcss postcss autoprefixer

COPY . .

CMD ["npm", "run", "dev"]
