# Shipment Schema

## Fields

- **startCoordinates** (Object, required)
  - **lat**: (Number, required) - The latitude of the starting point of the shipment.
  - **lon**: (Number, required) - The longitude of the starting point of the shipment.
- **endCoordinates** (Object, required)
  - **lat**: (Number, required) - The latitude of the ending point of the shipment.
  - **lon**: (Number, required) - The longitude of the ending point of the shipment.
- **pickupTime** (Object, required)
  - **date**: (Date, required) - The date of the pickup.
  - **hour**: (String, required) - The hour of the pickup, formatted as HH:MM.
- **typeOfShipment**: (String, required) - The type or category of the shipment.
- **weight**: (Number, required) - The weight of the shipment, assumed to be in kilograms or another preferred unit.
- **status**: (String, default: "undefined") - The current status of the shipment.

## Mongoose Schema Definition

```javascript
const mongoose = require('mongoose');

const ShipmentSchema = new mongoose.Schema({
  startCoordinates: {
    lat: {
      type: Number,
      required: true,
    },
    lon: {
      type: Number,
      required: true,
    },
  },
  endCoordinates: {
    lat: {
      type: Number,
      required: true,
    },
    lon: {
      type: Number,
      required: true,
    },
  },
  pickupTime: {
    date: {
      type: Date,
      required: true,
    },
    hour: {
      type: String, // format as HH:MM
      required: true,
    },
  },
  typeOfShipment: {
    type: String,
    required: true,
  },
  weight: {
    type: Number, // assuming weight is in kg or any unit you prefer
    required: true,
  },
  status: {
    type: String, 
    default: "undefined", // default status of the shipment
  }
});

module.exports = mongoose.model('Shipment', ShipmentSchema);
