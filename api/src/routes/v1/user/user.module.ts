import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { TestController } from './user.controller';
import { TestService } from './user.service';

@Module({
  imports: [ConfigModule.forRoot()],
  controllers: [TestController],
  providers: [TestService],
})
export class TestModule {}
