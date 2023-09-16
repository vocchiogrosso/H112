import { Injectable } from '@nestjs/common';

@Injectable()
export class V1Service {
  getHello(): string {
    return 'Hello from the V1 Stack!';
  }
}