import { Controller, Get, Post } from '@nestjs/common';
import { SharedService } from './shared.service';

@Controller('shared')
export class SharedController {
  constructor(private readonly sharedService: SharedService) {}

  @Get()
  getHello(): string {
    return this.sharedService.getHello();
  }

  @Post('login')
  searchUser(): string {
    return this.sharedService.searchUser();
  }
}
