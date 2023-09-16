import { Controller, Get } from '@nestjs/common';
import { ContractorService } from './contractor.service';

@Controller('contractor')
export class ContractorController {
  constructor(private readonly contractorService: ContractorService) {}

  @Get('')
  getHello(): string {
    return this.contractorService.getHello();
  }

}
