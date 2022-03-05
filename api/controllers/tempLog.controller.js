"use strict"

const TempLog = require("../models/temperatureLog.model")
const crypto = require('crypto');

const create = (req, res) => {
  const {
    temperature,
    air_humidity,
    lux,
    soil_humidity
  } = req.body;

  const entry = new TempLog({
    uuid: crypto.randomUUID(),
    temperature,
    air_humidity,
    lux,
    soil_humidity,
    created_at: new Date()
  })

  entry.save(function (err) {
    if (err) {
      if (err.code == 11000) {
        return res.status(422).json({ message: err.errmsg })
      } else {
        console.error(err)
        return res.status(500).json({ message: "Could not save new entry into database" })
      }
    }

    return res.status(200).json({ message: "Entry saved correctly" })
  })
}

const index = async (req, res) => {
  try {
    let { startDate, endDate } = req.query

    if (!startDate || !endDate) {
      return res.status(422).json({
        message: "The fields 'startDate' and 'endDate' are required.",
      })
    }

    const temperatureData = await TempLog.find({
      created: {
        $gte: new Date(startDate),
        $lt: new Date(`${endDate}T23:59:59Z`),
      },
    }).sort({ created: 1 })

    if (!temperatureData) {
      return res.status(404).json({
        message: "Could not retrieve data",
      })
    }

    return res.status(200).json({
      payload: temperatureData,
    })
  } catch (error) {
    console.error(error.message)

    return res.status(500).json({
      message: "Server error",
    })
  }
}

const lastEntry = async (req, res) => {
  try {
    const lastEntry = await TempLog.find().sort({ created: -1 }).limit(1)

    if (!lastEntry) {
      return res.status(404).json({
        message: "Could not retrieve data",
      })
    }

    return res.status(200).json({
      payload: lastEntry,
    })
  } catch (error) {
    console.error(error.message)

    return res.status(500).json({
      message: "Server error",
    })
  }
}

module.exports = {
  create,
  index,
  lastEntry,
}
