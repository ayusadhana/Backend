@echo off

REM Create directories
mkdir src
mkdir src\controllers
mkdir src\middlewares
mkdir src\models
mkdir src\routes
mkdir src\services
mkdir src\utils
mkdir src\constants

REM Create files
type nul > src\app.ts
type nul > src\middlewares\validation.ts
type nul > src\models\UserModel.ts
type nul > src\routes\userRoutes.ts
type nul > src\services\UserService.ts
type nul > src\utils\asyncWrapper.ts
type nul > src\utils\logger.ts
type nul > src\constants\httpStatusCodes.ts
type nul > src\constants\messagesConstants.ts
type nul > .env

echo File structure created successfully.
