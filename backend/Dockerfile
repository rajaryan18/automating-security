FROM node:16.16.0
WORKDIR C:\Docs\Python\automating-security\backend
COPY package*.json ./
RUN npm install
COPY . .
RUN npx hardhat run --network sepolia scripts/deploy.js
EXPOSE 3500
CMD ["npm", "start"]