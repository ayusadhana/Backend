// src/services/UserService.ts
import { IUser } from '../interfaces/IUser';
import { userModel } from '../models/UserModel';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

class UserService {
  async register(userDetails: IUser): Promise<string> {
    const hashedPassword = await bcrypt.hash(userDetails.passwordHash, 10);
    const user: IUser = await userModel.create({ ...userDetails, passwordHash: hashedPassword });
    // Generate JWT token
    const token = jwt.sign({ userId: user.id, phoneNumber: user.phoneNumber }, process.env.JWT_SECRET!, {
      expiresIn: '1h',
    });
    return token;
  }

  async login(phoneNumber: string, password: string): Promise<string | null> {
    const user: IUser | undefined = await userModel.findByPhoneNumber(phoneNumber);
    if (!user) {
      return null;
    }
    const isValidPassword = await bcrypt.compare(password, user.passwordHash);
    if (isValidPassword) {
      // Generate JWT token
      const token = jwt.sign({ userId: user.id, phoneNumber: user.phoneNumber }, process.env.JWT_SECRET!, {
        expiresIn: '1h',
      });
      return token;
    }
    return null;
  }
}

export const userService = new UserService();
