# API Components and Endpoints

## User Management

1. 
### `/api/users/register`
- **Method**: POST
- **Description**: This endpoint is designed to handle user registrations. Upon successful registration, the user's data will be stored in the database, with the role being set to "user" by default.
- **Body**: 
  - `_id`: Unique identifier for the user.
  - `name`: Full name of the user.
  - `email`: User's email address.
  - `password`: Password for account security.
- **Response Codes**:
  - `201`: Successfully created.
  - `400`: Bad request, details might be missing or invalid.
- **Returns**: 
  - A confirmation message upon successful registration.
  - JWT Token for authentication.

2. 
### `/api/users/login`
- **Method**: POST
- **Description**: This endpoint manages user login. It verifies the credentials provided by the users during the login process.
- **Body**:
  - `email`: User's email address for identification.
  - `password`: Corresponding password for authentication.
- **Response Codes**:
  - `200`: Successfully logged in.
  - `401`: Unauthorized, wrong credentials.
- **Returns**:
  - User details.
  - JWT Token for session management.

3. 
### `/api/users/dashboard`
- **Method**: GET
- **Description**: This endpoint fetches and displays the necessary information on the user's dashboard, providing a personalized user experience.
- **Headers**:
  - `Authorization`: Bearer `<JWT token>` to ensure only authenticated users access the data.
- **Response Codes**:
  - `200`: Successfully fetched the details.
  - `404`: Not found, incorrect user ID.
- **Returns**:
  - User's name, to be displayed prominently on the dashboard.
  - List of shipments linked with the user, to populate the 'View Previous Shipments' section.

## Shipment Management

4. 
### `/api/shipments/create`
- **Method**: POST
- **Description**: This endpoint facilitates the creation of a new shipment, storing all necessary shipment details as per the predefined schema.
- **Body**: Contains all shipment details as defined in your schema, including `startCoordinates`, `endCoordinates`, `pickupTime`, `typeOfShipment`, and `weight`.
- **Response Codes**:
  - `201`: Successfully created a new shipment.
  - `400`: Bad request, due to missing or incorrect details.
- **Returns**:
  - The created shipment details along with a unique shipment ID.

5. 
### `/api/shipments/pricing`
- **Method**: GET
- **Description**: This endpoint fetches the pricing details based on the entered shipment details. It also retrieves map information for displaying the start and end coordinates on a map.
- **Parameters**: 
  - `shipmentId`: Unique identifier for the shipment to fetch detailed pricing and map info.
- **Response Codes**:
  - `200`: Successfully retrieved pricing details.
  - `404`: Not found, incorrect shipment ID.
- **Returns**:
  - Pricing details including estimated cost.
  - Map information displaying the route from start to end coordinates.

6. 
### `/api/shipments/history`
- **Method**: GET
- **Description**: This endpoint fetches the history of shipments associated with a specific user, facilitating easy tracking and management of past shipments.
- **Parameters**:
  - `userId`: Unique identifier for the user.
- **Response Codes**:
  - `200`: Successfully retrieved the shipment history.
  - `404`: Not found, incorrect user ID.
- **Returns**:
  - A list of all shipments linked with the user, including detailed information on each shipment.

## Contractor Management

[ ]7. 
### `/api/contractors/dashboard`
- **Method**: GET
- **Description**: This endpoint gathers and displays relevant details on the contractor's dashboard, including a list of assigned shipments for easy management and tracking.
- **Headers**:
  - `Authorization`: Bearer `<JWT token>` to verify the contractor's identity.
- **Response Codes**:
  - `200`: Successfully fetched the details.
  - `404`: Not found, incorrect contractor ID.
- **Returns**:
  - List of   that needs to be retrieved.
- **Response Codes**:
  - `200`: Successfully retrieved shipment details.
  - `404`: Shipment not found, possibly incorrect shipment ID.
- **Returns**:
  - Detailed information about the selected shipment including pickup and drop locations, timings, and shipment contents.

9. 
### `/api/contractors/updateStatus`
- **Method**: PUT
- **Description**: This endpoint allows the contractor to update the status of a shipment, marking it as "complete" after successful delivery.
- **Body**: 
  - `shipmentId`: Unique identifier for the shipment.
  - `status`: New status to be updated ("complete").
- **Response Codes**:
  - `200`: Successfully updated the shipment status.
  - `400`: Bad request, due to incorrect data.
- **Returns**:
  - A confirmation message indicating successful status update.

## Notification Management (Potential Feature)

10. 
### `/api/notifications/create`
- **Method**: POST
- **Description**: This endpoint manages the creation of notifications to keep users updated about their shipment status in real-time.
- **Body**: 
  - `userId`: User's unique identifier.
  - `shipmentId`: Unique identifier for the shipment.
  - `message`: Notification message content.
- **Response Codes**:
  - `201`: Successfully created a new notification.
  - `400`: Bad request, due to missing or incorrect details.
- **Returns**:
  - A confirmation message indicating successful notification creation.

11. 
### `/api/notifications/fetch`
- **Method**: GET
- **Description**: This endpoint facilitates the retrieval of all notifications for a user, helping them stay informed about their shipments.
- **Parameters**: 
  - `userId`: User's unique identifier for fetching their notifications.
- **Response Codes**:
  - `200`: Successfully retrieved the notifications.
  - `404`: User not found or no notifications available.
- **Returns**:
  - A list of all notifications along with details like message content and timestamp.

## Shipment Status Management

12. 
### `/api/shipments/:id/status`
- **Method**: GET
- **Description**: Endpoint to fetch the current status of a particular shipment, facilitating real-time tracking.
- **Parameters**: 
  - `id`: Unique identifier for the shipment.
- **Response Codes**:
  - `200`: Successfully retrieved shipment status.
  - `404`: Shipment not found.
- **Returns**:
  - Current status of the shipment including location details (potential feature).

13. 
### `/api/shipments/:id/update`
- **Method**: PUT
- **Description**: This endpoint manages updates to shipment details, such as modifying the pickup time or altering the type of shipment.
- **Parameters**: 
  - `id`: Unique identifier for the shipment.
- **Body**:
  - Updated shipment details as per the schema.
- **Response Codes**:
  - `200`: Successfully updated the shipment details.
  - `400`: Bad request, due to incorrect or missing data.
- **Returns**:
  - A confirmation message indicating successful update of shipment details.

## User Profile Management

14. 
### `/api/users/:id/profile`
- **Method**: GET
- **Description**: Endpoint to retrieve the profile information of a user, which includes details like name and email.
- **Parameters**: 
  - `id`: Unique identifier for the user.
- **Response Codes**:
  - `200`: Successfully retrieved user profile information.
  - `404`: User not found.
- **Returns**:
  - Detailed user profile information including name, email, and other personal details.

15. 
### `/api/users/:id/update`
- **Method**: PUT
- **Description**: Endpoint to facilitate updates to the user's profile information, like changing the name or email.
- **Parameters**: 
  - `id`: Unique identifier for the user.
- **Body**:
  - Updated user details like name, email etc.
- **Response Codes**:
  - `200`: Successfully updated user profile.
  - `400`: Bad request due to incorrect or missing data.
- **Returns**:
  - A confirmation message indicating successful update of user details.

16. 
### `/api/users/:id/delete`
- **Method**: DELETE
- **Description**: Endpoint to delete a user's profile, with necessary authentication and authorization checks to ensure data security.
- **Parameters**: 
  - `id`: Unique identifier for the user.
- **Response Codes**:
  - `200`: Successfully deleted user profile.
  - `403`: Forbidden, user is not authorized to perform the deletion.
  - `404`: User not found.
- **Returns**:
  - A confirmation message indicating successful deletion of user profile.

## Contractor Profile Management

17. 
### `/api/contractors/:id/profile`
- **Method**: GET
- **Description**: Endpoint to retrieve the profile information of a contractor, providing details like name and associated company.
- **Parameters**: 
  - `id`: Unique identifier for the contractor.
- **Response Codes**:
  - `200`: Successfully retrieved contractor profile information.
  - `404`: Contractor not found.
- **Returns**:
  - Detailed contractor profile information including name, email, and company details.

18. 
### `/api/contractors/:id/update`
- **Method**: PUT
- **Description**: Endpoint to facilitate updates to the contractor's profile information, such as changing the name or email.
- **Parameters**: 
  - `id`: Unique identifier for the contractor.
- **Body**:
  - Updated contractor details like name, email etc.
- **Response Codes**:
  - `200`: Successfully updated contractor profile.
  - `400`: Bad request due to incorrect or missing data.
- **Returns**:
  - A confirmation message indicating successful update of contractor details.

19. 
### `/api/contractors/:id/delete`
- **Method**: DELETE
- **Description**: Endpoint to delete a contractor's profile, including necessary authentication and authorization checks to ensure data security.
- **Parameters**: 
  - `id`: Unique identifier for the contractor.
- **Response Codes**:
  - `200`: Successfully deleted contractor profile.
  - `403`: Forbidden, contractor is not authorized to perform the deletion.
  - `404`: Contractor not found.
- **Returns**:
  - A confirmation message indicating successful deletion of contractor profile.

## Real-time Tracking (Potential Feature)

20. 
### `/api/shipments/:id/track`
- **Method**: GET
- **Description**: This endpoint allows for real-time tracking of a shipment, providing updated location and status information.
- **Parameters**: 
  - `id`: Unique identifier for the shipment.
- **Response Codes**:
  - `200`: Successfully retrieved real-time tracking information.
  - `404`: Shipment not found.
- **Returns**:
  - Real-time tracking information, including current location and status of the shipment.

21. 
### `/api/notifications/:id`
- **Method**: DELETE
- **Description**: Endpoint to delete a specific notification after it has been viewed or upon user request, helping to maintain a clean notification history.
- **Parameters**: 
  - `id`: Unique identifier for the notification.
- **Response Codes**:
  - `200`: Successfully deleted the notification.
  - `404`: Notification not found.
- **Returns**:
  - A confirmation message indicating successful deletion of the notification.
