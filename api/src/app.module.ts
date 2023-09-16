import { Module } from '@nestjs/common';
import { MongodbModule } from 'src/database/mongodb/mongodb.module';
import { AppController } from './app.controller';
import { AppService } from './app.service';

import { V1Module } from './routes/v1/v1.module';

@Module({
  imports: [MongodbModule, V1Module ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
