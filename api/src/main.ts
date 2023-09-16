import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ExpressAdapter } from '@nestjs/platform-express';
import * as chalk from 'chalk';
import * as express from 'express';
import * as dotenv from 'dotenv';
import * as path from 'path';
import corsConfig from './config/cors.config';

dotenv.config({path: '.env.development'});

async function bootstrap() {
  const server = express();
  const app = await NestFactory.create(AppModule, new ExpressAdapter(server));
  app.enableCors(corsConfig);
  const port = process.env.PORT || 8000;
  await app.listen(port);
  console.log(chalk.red(`API`)+` is listening in`+` ${process.env.NODE_ENV} ENV on `+chalk.blue(`http://localhost:${port}/`));
  }
bootstrap();