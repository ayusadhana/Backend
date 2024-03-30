// src/routes/userRoutes.ts
import express from 'express';
import { userController } from '../controllers/UserController';
import { userRegistrationValidator, userLoginValidator } from '../middlewares/validation';
import { verifyToken } from '../middlewares/verifyToken';

const router = express.Router();

router.post('/register', userRegistrationValidator, userController.register);
router.post('/login', userLoginValidator, userController.login);

// Protected route example
router.get('/profile', verifyToken, userController.getProfile);

export default router;
