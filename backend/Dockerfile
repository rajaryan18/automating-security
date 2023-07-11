FROM node:16.16.0
WORKDIR C:\Docs\Python\automating-security\backend
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5000
CMD ["npm", "start"]