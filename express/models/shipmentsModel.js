const mongoose = require('mongoose')

const Schema = mongoose.Schema

const shipmentSchema = new Schema({
    title: {
        type: String,
        required: true
    },
    startCoordinates: {
        lng: {
            type: String,
            required: true
        },
        ltd: {
            type: String,
            required: true
        }
    },
    endCoordinates: {
        lng: {
            type: String,
            required: true
        },
        ltd: {
            type: String,
            required: true
        }
    },
    pickupTime: {
        type: Number,
        required: true
    },
    typeOfShipment: {
        type: String,
        required: true
    },
    weight: {
        type: String,
        required: true
    },
    pricing: {
        type: String,
        required: true
    },
    user_id: {
        type: String,
        required: true
    }
}, { timestamps: true })

module.exports = mongoose.model('shipment', shipmentSchema)