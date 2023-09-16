import { Controller, Get } from '@nestjs/common';

@Controller('v1')
export class V1Controller {
  constructor() {}

  @Get('')
  getUserData(): string {
    return 'Version 1 - User Data';
  }
}
