import { Body, Controller, Get, Post } from '@nestjs/common';
import { TestService } from './test.service';
import { RequestDto } from './request.dto';

@Controller('test')
export class TestController {
  constructor(private readonly myService: TestService) {}


  @Get()
  async getEndpoint() {
    //const result = await this.myService.invokeLambdaFunction();
    return 200;
  }

  @Post('calculate')
  async postEndpoint(@Body() RequestDto: any){
    const result = await this.myService.invokeLambdaFunction(RequestDto);
    return result;
  }

}
