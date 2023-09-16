import { Body, Controller, Get, Post } from '@nestjs/common';
import { ContractorService } from './contractor.service';

@Controller('contractor')
export class ContractorController {
  constructor(private readonly myService: ContractorService) {}


  @Get()
    test() {
      return test
    }
}
