import { Controller, Post, Get, Body, Request, UseGuards } from '@nestjs/common';
import { UserService } from './user.service';
import { JwtAuthGuard } from '../../../common/guards/auth-guards';

@Controller('/users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get('')
  test():number{
    return 200
  }

  @Post('/register')
  async register(@Body() userData: any): Promise<any> {
    return this.userService.register(userData);
  }

  @Post('/login')
  async login(@Body() userData: any): Promise<any> {
    return this.userService.login(userData);
  }

  @UseGuards(JwtAuthGuard)
  @Get('/dashboard')
  async dashboard(@Request() req: any): Promise<any> {
    return this.userService.dashboard(req.user.userId);
  }
}
