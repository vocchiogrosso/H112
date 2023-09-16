import { Module } from '@nestjs/common';

import { MongodbModule } from 'src/database/mongodb/mongodb.module';

import { AppController } from './app.controller';
import { AppService } from './app.service';

import { V1Module } from './v1/v1.module'; // Import the V1Module

//import { AuthModule } from 'src/auth/auth.module'; 
//import { PostModule } from 'src/post/post.module';
//import { UserModule } from 'src/user/user.module';

@Module({
  imports: [MongodbModule, V1Module ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
