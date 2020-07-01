'use strict'

const express = require('express')
const tempLogController = require('../controllers/tempLog.controller')
const router = express.Router();

router.post('/logData', tempLogController.save);
router.get('/temperatureData', tempLogController.get);
router.get('/lastEntry', tempLogController.lastEntry);

module.exports = router;