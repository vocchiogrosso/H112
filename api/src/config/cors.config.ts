// cors.config.ts
import { CorsOptions } from 'cors';

const corsConfig: CorsOptions = {
  origin: 'http://example.com',
  methods: ['GET', 'POST'],
  allowedHeaders: ['Content-Type', 'Authorization'],
};

export default corsConfig;