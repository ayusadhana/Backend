import express, { Application, Request, Response, NextFunction } from 'express';
import bodyParser from 'body-parser';
import { errorHandler } from './middlewares/errorHandler';
import { userRoutes } from './routes/userRoutes';

// Create Express application
const app: Application = express();

// Middleware
app.use(bodyParser.json());

// Routes
app.use('/api/users', userRoutes);

// Error handler middleware
app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
    errorHandler(err, req, res, next);
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
