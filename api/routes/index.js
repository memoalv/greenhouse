'use strict'

const express = require('express')
const router = express.Router();

router.use('/climate', require('./climate.routes'));

module.exports = router;