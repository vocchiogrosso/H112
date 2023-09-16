import { Module } from '@nestjs/common';
import { MongodbModule } from '../../../database/mongodb/mongodb.module';
import { UserSchema } from '../../../common/schema/user.schema';  // Adjust the path as necessary
import { UserService } from './user.service';
import { UserController } from './user.controller';
import { JwtModule } from '@nestjs/jwt';  // Import JwtModule

@Module({
  imports: [
    MongodbModule,
    JwtModule.register({
      secret: 'yourSecretKey',  // replace with your secret key
      signOptions: { expiresIn: '60s' },  // adjust as necessary
    }),
  ],
  providers: [UserService],
  controllers: [UserController],
})
export class UserModule {}
