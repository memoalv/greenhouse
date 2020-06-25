"use strict"

const TempLog = require("../models/temperatureLog.model")

const save = (req, res) => {
  const entry = new TempLog(req.body)

  entry.save(function (err) {
    if (err) {
      if (err.code == 11000) {
        return res.status(422).json({ message: err.errmsg })
      }
      else {
        console.error(err)
        return res.status(500).json({ message: "Could not save new entry into database" })
      }
    }

    return res.status(200).json({ message: "Entry saved correctly" })
  })
}

module.exports = {
  save,
}
