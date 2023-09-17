import { Controller, Post, Body, Get, Req, HttpCode, HttpException, HttpStatus, UseGuards } from '@nestjs/common';
import { UserService } from './user.service';
import { JwtAuthGuard } from './jwt-auth.guard';
import { UserDto, LoginDto } from './user.dto';

@Controller('v1/user')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post('register')
  @HttpCode(HttpStatus.CREATED)
  async register(@Body() userDto: UserDto) {
    const result = await this.userService.register(userDto);
    if (result.success) {
      return {
        message: result.message,
        token: result.token,
      };
    } else {
      throw new HttpException(result.message || 'Registration failed', HttpStatus.BAD_REQUEST);
    }
  }
  
  @Post('login')
  async login(@Body() loginDto: LoginDto) {
    const result = await this.userService.login(loginDto.email, loginDto.password);
    if (result.success) {
      return {
        user: result.user,
        token: result.token,
      };
    } else {
      throw new HttpException(result.message, HttpStatus.UNAUTHORIZED);
    }
  }

  @UseGuards(JwtAuthGuard)
  @Get('dashboard')
  async dashboard(@Req() req) {
    const result = await this.userService.getDashboard(req.user._id);
    if (result.success) {
      return {
        name: result.name,
        shipments: result.shipments,
      };
    } else {
      throw new HttpException(result.message, HttpStatus.NOT_FOUND);
    }
  }
}
