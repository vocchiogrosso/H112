import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class ContractorService {

  async test() {
    return 200
  }
  
}
