const User = require('../models/userModel')
const jwt = require('jsonwebtoken')

const createToken = (_id) => {
    return jwt.sign({_id: _id}, process.env.SECRET, { expiresIn: '1d' })
}

// login a user
const loginUser = async (req, res) => {
    const {email, password} = req.body

    try {
        const user = await User.login(email, password)

        // create a token
        const token = createToken(user._id)

        res.status(200).json({name: user.name, email, token, role: user.role, _id:user._id})
    } catch (error) {
        res.status(400).json({error: error.message})
    }
}

// signup a user
const signupUser = async (req, res) => {
    const {name, email, password, role} = req.body

    try {
        const user = await User.signup(name, email, password, role)

        // create a token
        const token = createToken(user._id)

        res.status(200).json({name, email, token, role: user.role, _id:user._id})
    } catch (error) {
        res.status(400).json({error: error.message})
    }

}

module.exports = { signupUser, loginUser }