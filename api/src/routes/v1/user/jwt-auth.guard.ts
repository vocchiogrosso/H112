import { Injectable, ExecutionContext, UnauthorizedException } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import * as jwt from 'jsonwebtoken';

@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {
  canActivate(context: ExecutionContext) {
    
  }

  handleRequest(err, user, info) {
    // handle your authentication error here
    if (err || !user) {
      throw err || new UnauthorizedException();
    }
    return user;
  }
}
