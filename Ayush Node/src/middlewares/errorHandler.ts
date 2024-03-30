// src/middlewares/errorHandler.ts
import { Request, Response, NextFunction } from 'express';
import logger from '../utils/logger';

interface IErrorResponse {
  status: string;
  message: string;
  stack?: string;
}

export const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  const response: IErrorResponse = {
    status: 'error',
    message: err.message,
  };

  if (process.env.NODE_ENV === 'development') {
    response.stack = err.stack;
  }

  logger.error(err.message, { stack: err.stack, path: req.path });

  const statusCode = res.statusCode === 200 ? 500 : res.statusCode; // If statusCode not set, default to 500
  res.status(statusCode).json(response);
};
