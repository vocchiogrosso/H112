import { Module } from '@nestjs/common';

import { MongodbModule } from 'src/database/mongodb/mongodb.module';

import { AppController } from './app.controller';
import { AppService } from './app.service';



//import { AuthModule } from 'src/auth/auth.module'; 
//import { PostModule } from 'src/post/post.module';
//import { UserModule } from 'src/user/user.module';

@Module({
  imports: [MongodbModule ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
