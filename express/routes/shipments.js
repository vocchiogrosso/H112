const express = require('express')
const requireAuth = require('../middleware/requireAuth')
const {getShipments, getShipment, createShipment} = require("../controllers/shipmentController");

const router = express.Router()

// require auth for all shipment routes
router.use(requireAuth)

// GET all shipment
router.get('/getAll/:id' , getShipments)

// GET a single shipment
router.get('/get/:id', getShipment)

// POST a new shipment
router.post('/create', createShipment)


module.exports = router