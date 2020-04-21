'use strict'

const express = require('express')
const usersController = require('../../controllers/users.controller')
const router = express.Router();
const authMiddleware = require('../../middlewares/auth')

router.post('/signUp', usersController.signUp);
router.post('/signIn', usersController.signIn);
router.post('/test', authMiddleware, usersController.test);

module.exports = router;