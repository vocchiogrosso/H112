require('dotenv').config()

const express = require('express')
const mongoose = require("mongoose");
const cors = require('cors'); // Add this line
const shipmentsRoutes = require('./routes/shipments')
const userRoutes = require('./routes/user')

const app = express()

// Middleware
app.use(express.json())
app.use(cors(  {origin: 'http://localhost:5173'})); // Enable CORS for all routes

app.use((req, res, next) => {
    console.log(req.path, req.method)
    next()
})

// Routes
app.use('/api/user', userRoutes)
app.use('/api/shipments', shipmentsRoutes)

// Connect to the database
mongoose.connect(process.env.MONGO_URI)
    .then(() => {
        // Listen for requests
        app.listen(process.env.PORT, () => {
            console.log('Connected to db & listening on port', process.env.PORT)
        })
    })
    .catch((error) => {
        console.log(error)
    })
