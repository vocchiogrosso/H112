import * as bcrypt from 'bcrypt';
import { Schema, Document, model } from 'mongoose';

export interface UserDocument extends Document {
  _id: string;
  name: string;
  email: string;
  password: string;
  role: string;
  shipments?: any[];
  comparePassword(candidatePassword: string, cb: any): void;
}

export const UserSchema = new Schema<UserDocument>({
  _id: { type: String, required: true },
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  role: { type: String, required: true },
  shipments: { type: [], required: false, default: [] },
});

UserSchema.methods.comparePassword = function(candidatePassword: string, cb: any) {
  bcrypt.compare(candidatePassword, this.password, (err: Error, isMatch: boolean) => {
    if (err) return cb(err);
    cb(null, isMatch);
  });
};

export const User = model<UserDocument>('User', UserSchema);
