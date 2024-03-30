// src/models/UserModel.ts
import { getRepository } from "typeorm";
import { User } from "../entity/User";
import { IUser } from "../interfaces/IUser";

class UserModel {
  async create(userData: IUser): Promise<IUser> {
    const userRepository = getRepository(User);
    const user: IUser = userRepository.create(userData);
    await userRepository.save(user);
    return user;
  }

  async findByPhoneNumber(phoneNumber: string): Promise<IUser | undefined> {
    const userRepository = getRepository(User);
    return await userRepository.findOne({ phoneNumber });
  }
}

export const userModel = new UserModel();
