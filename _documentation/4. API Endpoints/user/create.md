# User Creation API Endpoint

This documentation outlines the usage and functionality of the User Creation API endpoint in our NestJS application.

## Endpoint

- **URL**: `/api/users`
- **HTTP Method**: `POST`

## Request

### Headers

No specific headers are required for this endpoint.

### Body

- **Content Type**: `application/json`

#### Request Body Example

```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "password123"
}
