// src/middlewares/validation.ts
import { body, ValidationChain } from 'express-validator';

export const userRegistrationValidator: ValidationChain[] = [
  body('name').trim().notEmpty(),
  body('phoneNumber').trim().isMobilePhone('any'),
  body('password').trim().isLength({ min: 6 }),
];

export const userLoginValidator: ValidationChain[] = [
  body('phoneNumber').trim().isMobilePhone('any'),
  body('password').trim().isLength({ min: 6 }),
];
