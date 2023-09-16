# User Schema

### Fields

- `_id`: (String, required) - Unique identifier for each user.
- `name`: (String, required) - The name of the user.
- `email`: (String, required, unique) - The email of the user.
- `password`: (String, required) - The user's password.
- `role`: (String, required) - The role assigned to the user.

### Mongoose Schema Definition

```javascript
const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  _id: {
    type: String,
    required: true,
  },
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
  role: {
    type: String,
    required: true,
  }
});

module.exports = mongoose.model('User', UserSchema);
