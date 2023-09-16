# User Management API Endpoints

This documentation outlines the usage and functionality of the User Management API endpoints in our NestJS application.

## Update User

### Endpoint

- **URL**: `/api/users/:id`
- **HTTP Method**: `PUT`

### Request

#### Headers

No specific headers are required for this endpoint.

#### URL Parameters

- `id` (number, required): The unique identifier of the user to be updated.

#### Request Body

- **Content Type**: `application/json`

##### Request Body Example

```json
{
  "username": "updated_username",
  "email": "updated@example.com"
}
