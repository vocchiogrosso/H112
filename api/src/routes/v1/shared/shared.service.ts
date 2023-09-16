import { Injectable } from '@nestjs/common';

@Injectable()
export class SharedService {
  getHello(): string {
    return 'Hello from the Shared Service!';
  }
  searchUser(): string {
    return "Test"
  }
}