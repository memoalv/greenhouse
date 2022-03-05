'use strict'

const express = require('express')
const tempLogController = require('../controllers/tempLog.controller')
const router = express.Router();

router.post('/', tempLogController.create);
router.get('/', tempLogController.index);
router.get('/last_entry', tempLogController.lastEntry);

module.exports = router;