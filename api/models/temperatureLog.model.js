"use strict"

const mongoose = require("mongoose")
const Schema = mongoose.Schema

const tempLogSchema = new Schema(
  {
    uuid: {
      type: String,
      unique: true,
    },
    temperature: Number,
    air_humidity: Number,
    lux: Number,
    soil_humidity: Number,
    created: Date,
  },
  { collection: "tempLog" }
)

module.exports = mongoose.model("TempLog", tempLogSchema)
