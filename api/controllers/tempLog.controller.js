"use strict"

const TempLog = require("../models/temperatureLog.model")

const save = (req, res) => {
  const entry = new TempLog(req.body)

  entry.save(function (err) {
    
    if (err) {
      console.log(err)
      res.status(500).send({ message: "Could not save new entry into database" })
    }

    return res.status(200).send({ message: "Entry saved correctly" })
  })
}

module.exports = {
  save,
}
