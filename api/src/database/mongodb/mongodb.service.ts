import { Injectable } from '@nestjs/common';
import { MongoClient, Db } from 'mongodb';
import { mongodbConfig } from './mongodb.config';

@Injectable()
export class MongodbService {
  private client: MongoClient;
  private db: Db;

  async connect(): Promise<Db> {
    try {
      this.client = new MongoClient(mongodbConfig.uri);
      await this.client.connect();
      this.db = this.client.db();
      console.log('Connected to MongoDB');
      return this.db;
    } catch (error) {
      console.error('Failed to connect to MongoDB:', error);
      throw error;
    }
  }

  async disconnect(): Promise<void> {
    if (this.client) {
      await this.client.close();
      console.log('Disconnected from MongoDB');
    }
  }
}
