import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import * as AWS from 'aws-sdk';

@Injectable()
export class TestService {
  private lambda: AWS.Lambda;

  constructor(private configService: ConfigService) {
    this.lambda = new AWS.Lambda({
      region: this.configService.get<string>('AWS_REGION'),
      accessKeyId: this.configService.get<string>('AWS_ACCESS_KEY_ID'),
      secretAccessKey: this.configService.get<string>('AWS_SECRET_ACCESS_KEY'),
    });
  }

  async invokeLambdaFunction(payload: object) {
    const params: AWS.Lambda.InvocationRequest = {
      FunctionName: 'haversine',  // replace with your function's name
      Payload: JSON.stringify(payload)
    };

    try {
      const data = await this.lambda.invoke(params).promise();
      return data.Payload;
    } catch (error) {
      console.error(JSON.stringify(error));
      throw error;
    }
  }
}
