import { Injectable } from '@nestjs/common';

@Injectable()
export class ContractorService {
  getHello(): string {
    return 'Hello from the Contractor Service!';
  }
}