import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ContractorController } from './contractor.controller';
import { ContractorService } from './contractor.service';

@Module({
  imports: [ConfigModule.forRoot()],
  controllers: [ContractorController],
  providers: [ContractorService],
})
export class ContractorModule {}
