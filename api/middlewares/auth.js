"use strict"

function authorized(req, res, next) {
  if (!req.headers.authorization) {
    return res.status(403).send()
  }

  if (req.headers.authorization === process.env.AUTH_KEY) {
    next()
  } else {
    return res.status(403).send()
  }
}

module.exports = authorized
