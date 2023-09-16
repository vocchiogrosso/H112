const Shipment = require('../models/shipmentsModel')
const mongoose = require('mongoose')
// get all workouts
const getShipments = async (req,res) => {
    const user_id = req.user._id

    const shipment = await Shipment.find({user_id}).sort({pickupTime: -1})

    res.status(200).json(shipment)
}
// get a single workout
const getShipment = async (req,res) => {
    const {id} = req.params
    if (!mongoose.Types.ObjectId.isValid(id)){
        return res.status(404).json({error: ' No such Shipment'})
    }

    const shipment = await Shipment.findById(id)

    if (!shipment) {
        return res.status(404).json({error: 'No such shipment'})
    }
    res.status(200).json(shipment)
}
// create new workout
const createShipment = async (req, res) => {
    const {title, startCoordinates, endCoordinates, pickupTime, typeOfShipment, weight, pricing} = req.body

    let emptyFields = []

    if(!title) {
        emptyFields.push('title')
    }
    if(!startCoordinates) {
        emptyFields.push('startCoordinates')
    }
    if(!endCoordinates) {
        emptyFields.push('endCoordinates')
    }
    if(!pickupTime) {
        emptyFields.push('pickupTime')
    }
    if(!typeOfShipment) {
        emptyFields.push('typeOfShipment')
    }
    if(!weight) {
        emptyFields.push('weight')
    }
    if(!pricing) {
        emptyFields.push('pricing')
    }
    if(emptyFields.length > 0){
        return res.status(400).json({ error: "Please fill in all the fields", emptyFields })
    }
    //add doc to db
    try {
        const user_id = req.user._id
        const shipment = await Shipment.create({title, startCoordinates, endCoordinates, pickupTime, typeOfShipment, weight, pricing, user_id})
        res.status(200).json(shipment)
    } catch (error) {
        res.status(400).json({error: error.message})
    }
}

module.exports = {
    createShipment, getShipment, getShipments
}