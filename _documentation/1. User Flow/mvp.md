# Flow

## Pages and Components Definition

### /auth
- **Components**
  - Login Form: contains fields for email and password
  - Registration Form: contains fields like _id, name, email, and password, with role defaulted to "user"

### /user/dashboard
- **Components**
  - User Information Display: shows the user's name
  - Shipment History Component: displays a list of past shipments

### /shipment/create
- **Components**
  - Shipment Creation Form: contains fields for defining shipment details as per your schema

### /shipment/pricing
- **Components**
  - Pricing Details Component: displays calculated pricing based on the shipment details
  - Map Display Component: visualizes the start and end coordinates, along with the planned route

### /contractor/dashboard
- **Components**
  - Schedule Component: showcases all the currently assigned shipments

### /contractor/schedule
- **Components**
  - Shipment Details Component: provides detailed information on the selected shipment
  - Navigation Map Component: provides route information and allows for status updates

## Flow Stages

### Stage 1: Registration and Login
1. **Visitor**: Accesses the /auth page, where they can choose between Login and Register components.
2. **Visitor**: Registers by filling out the registration form, with the role automatically set to "user".
3. **Visitor**: Logs in using the new credentials.

### Stage 2: User Dashboard and Shipment Creation
4. **User**: Lands on the /user/dashboard after a successful login, where the user's name is prominently displayed.
5. **User**: Can either initiate a new shipment creation via the shipment creation form or review their shipment history through the shipment history component.
6. **User**: Fills in the necessary details in the shipment creation form and submits it, transitioning to the /shipment/pricing page for review and confirmation of pricing and map details.
7. **User**: Confirms the shipment, leading them back to the dashboard where they can observe all their shipments, including the new entry, through the shipment history component.

### Stage 3: Contractor Dashboard and Schedule Management
8. **Contractor**: Logs in and navigates to the /contractor/dashboard, which contains a schedule component showcasing all the currently assigned shipments.
9. **Contractor**: Selects a specific shipment to view more details, which takes them to the /contractor/schedule page showcasing detailed shipment information.

### Stage 4: Shipment Navigation and Completion
10. **Contractor**: Utilizes the navigation map component for detailed route information between the start and end coordinates, aiding in efficient route planning and management of the delivery.
11. **Contractor**: After successfully delivering the shipment, uses the Complete option on the navigation map component to update the shipment status to "complete".

### Stage 5: User Notifications and Tracking
12. **User**: At any time, can track the real-time status of their shipments via the shipment history component, which provides a detailed view of each shipment's status and history.
13. **User**: Receives a notification (potential feature) about the completion of the shipment and can now view the "complete" status on their dashboard.
