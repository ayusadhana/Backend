// src/server.ts
import express, { Express } from 'express';
import userRoutes from './routes/userRoutes';
import { errorHandler } from './middlewares/errorHandler';
import "reflect-metadata";
import { createConnection } from "typeorm";

const app: Express = express();
const port: number | string = process.env.PORT || 3000;

app.use(express.json());
app.use('/v1/users', userRoutes);
app.use(errorHandler); // Use the error handling middleware

createConnection().then(() => {
  app.listen(port, () => {
    console.log(`Server running on port ${port}`);
  });
}).catch(error => console.error(error));
