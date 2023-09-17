import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';

import { UserController } from './user.controller';
import { UserService } from './user.service';
import { UserSchema } from './user.schema';
import { JwtModule } from '@nestjs/jwt';
import { JwtAuthGuard } from './jwt-auth.guard';

@Module({
  imports: [
    MongooseModule.forFeature([{ name: 'User', schema: UserSchema }]),
    JwtModule.register({
      secret: "MY_SECRET_KEY", // Replace with your own secret key
      signOptions: { expiresIn: '60m' },
    }),
  ],
  controllers: [UserController],
  providers: [
    UserService,
    JwtAuthGuard,
  ],
  exports: [UserService],
})
export class UserModule {}
