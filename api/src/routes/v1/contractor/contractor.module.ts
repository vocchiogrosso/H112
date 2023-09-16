import { Module } from '@nestjs/common';
import { ContractorController } from './contractor.controller';
import { ContractorService } from './contractor.service';

@Module({
  imports:[],
  controllers: [ContractorController],
  providers: [ContractorService],
})
export class ExampleModule {}