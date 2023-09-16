# User Management API Endpoints

This documentation outlines the usage and functionality of the User Management API endpoints in our NestJS application.

## Delete User

### Endpoint

- **URL**: `/api/users/:id`
- **HTTP Method**: `DELETE`

### Request

#### Headers

No specific headers are required for this endpoint.

#### URL Parameters

- `id` (number, required): The unique identifier of the user to be deleted.

### Response

#### Success Response

- **Status Code**: `204 No Content`

#### Error Responses

- **Status Code**: `404 Not Found`
  - **Response Body Example** (User Not Found):
    ```json
    {
      "statusCode": 404,
      "message": "User not found",
      "error": "Not Found"
    }
    ```

- **Status Code**: `500 Internal Server Error`
  - **Response Body Example** (Internal Server Error):
    ```json
    {
      "statusCode": 500,
      "message": "Internal server error",
      "error": "Internal Server Error"
    }
    ```

## Usage

To delete a user, make a DELETE request to the `/api/users/:id` endpoint. Upon success, you will receive a `204 No Content` response indicating that the user has been deleted.

Example using `curl` for deleting a user:

```bash
curl -X DELETE http://localhost:3000/api/users/1
