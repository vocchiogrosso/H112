import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { User, UserDocument } from '../../../common/schema/user.schema';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class UserService {
  constructor(
    @InjectModel(User.name) private userModel: Model<UserDocument>,
    private jwtService: JwtService,
  ) {}

  async register(userData: any): Promise<any> {
    const createdUser = new this.userModel(userData);
    await createdUser.save();

    const payload = { username: createdUser.name, sub: createdUser._id };
    return {
      message: 'Successfully registered',
      token: this.jwtService.sign(payload),
    };
  }

  async login(userData: any): Promise<any> {
    const user = await this.userModel.findOne({ email: userData.email });
    if (!user) {
      throw new Error('Invalid email or password');
    }
  
    const isMatch: boolean = await new Promise((resolve, reject) => {
      user.comparePassword(userData.password, (err: Error, isMatch: boolean) => {
        if (err) {
          reject(err);
        } else {
          resolve(isMatch);
        }
      });
    });
  
    if (!isMatch) {
      throw new Error('Invalid email or password');
    }
  
    const payload = { username: user.name, sub: user._id };
    return {
      user,
      token: this.jwtService.sign(payload),
    };
  }
  

  async dashboard(userId: string): Promise<any> {
    const user = await this.userModel.findById(userId).populate('shipments');
    if (!user) {
      throw new Error('User not found');
    }

    return {
      name: user.name,
      shipments: user.shipments,
    };
  }
}

