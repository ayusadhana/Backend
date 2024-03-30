// src/controllers/UserController.ts
import { Request, Response } from 'express';
import { userService } from '../services/UserService';
import { validationResult } from 'express-validator';
import { HttpStatusCodes } from '../constants/httpStatusCodes';
import * as Messages from '../constants/messagesConstants';
import { asyncWrapper } from '../utils/asyncWrapper';

export class UserController {
  register = asyncWrapper(async (req: Request, res: Response): Promise<void> => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(HttpStatusCodes.BAD_REQUEST).json({ errors: errors.array() });
    }

    try {
      const user = await userService.register(req.body);
      res.status(HttpStatusCodes.CREATED).json({ message: Messages.MSG_USER_CREATED_SUCCESS, user });
    } catch (error) {
      res.status(HttpStatusCodes.INTERNAL_SERVER_ERROR).json({ message: Messages.MSG_INTERNAL_SERVER_ERROR });
    }
  });

  login = asyncWrapper(async (req: Request, res: Response): Promise<void> => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(HttpStatusCodes.BAD_REQUEST).json({ errors: errors.array() });
    }

    const { phoneNumber, password } = req.body;
    const isValid = await userService.login(phoneNumber, password);
    if (isValid) {
      res.status(HttpStatusCodes.OK).json({ message: Messages.MSG_LOGIN_SUCCESS });
    } else {
      res.status(HttpStatusCodes.UNAUTHORIZED).json({ message: Messages.MSG_UNAUTHORIZED });
    }
  });
}
