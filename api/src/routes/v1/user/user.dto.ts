export class UserDto {
  _id: string;
  name: string;
  email: string;
  password: string;
  role?: string;
  shipments?: any[];
}

export class LoginDto {
  email: string;
  password: string;
}

export class DashboardDto {
  authorization: string;
}
