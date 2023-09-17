import { Injectable, HttpException, HttpStatus } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { JwtService } from '@nestjs/jwt';
import { UserDocument } from './user.schema';
import { UserDto } from './user.dto';
import * as bcrypt from 'bcrypt';

@Injectable()
export class UserService {
  constructor(
    @InjectModel('User') private userModel: Model<UserDocument>,
    private readonly jwtService: JwtService,
  ) {}

  async findUserByEmail(email: string): Promise<UserDocument | null> {
    return await this.userModel.findOne({ email });
  }

  async register(userDto: UserDto) {
    const hashedPassword = await bcrypt.hash(userDto.password, 10);
    const createdUser = new this.userModel({
      ...userDto,
      password: hashedPassword,
    });

    try {
      const savedUser = await createdUser.save();
      const payload = { username: savedUser.name, sub: savedUser._id };
      const token = this.jwtService.sign(payload);
      return {
        success: true,
        message: 'User successfully registered',
        token,
      };
    }catch (error) {
      throw new HttpException({ message: error.message, success: false }, HttpStatus.BAD_REQUEST);
    }
  }      
  

  async login(email: string, password: string) {
    try {
      const user = await this.userModel.findOne({ email });
      if (user && (await bcrypt.compare(password, user.password))) {
        const payload = { username: user.name, sub: user._id };
        const token = this.jwtService.sign(payload);
        return {
          success: true,
          user,
          token,
        };
      } else {
        return {
          success: false,
          message: 'Invalid credentials',
        };
      }
    } catch (error) {
      throw new HttpException(error.message, HttpStatus.UNAUTHORIZED);
    }
  }

  async getDashboard(userId: string) {
    try {
      const user = await this.userModel.findById(userId).select('-password');
      if (user) {
        return {
          success: true,
          name: user.name,
          shipments: user.shipments,
        };
      } else {
        return {
          success: false,
          message: 'User not found',
        };
      }
    } catch (error) {
      throw new HttpException(error.message, HttpStatus.NOT_FOUND);
    }
  }
}
