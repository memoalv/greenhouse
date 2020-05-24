"use strict"

function authorized(req, res, next) {
  if (!req.headers.authorization) {
    return res.status(403).send()
  }
  
  req.headers.authorization == "59f02390-a2a3-4dc1-b19d-3c37d8933fa0" ? next() : res.status(403)
}

module.exports = authorized
