'use strict'

const express = require('express')
const router = express.Router();

router.use('/auth', require('./users/auth.routes'));

module.exports = router;