'use strict'

const jwt = require('jwt-simple');
const moment = require('moment');
const config = require('../config');

function createToken(user) {
    const payload = {
        sub: user.uuid,
        iat: moment().unix(),
        exp: moment().add(12, 'hours').unix()
    }

    return jwt.encode(payload, config.SECRET_TOKEN)
}

function decodeToken(token) {
    const decoded = new Promise((resolve, reject) => {
        try {
            const payload = jwt.decode(token, config.SECRET_TOKEN)

            if (payload.exp <= moment().unix()) {
                reject({
                    status: 401,
                    message: "El token ha expirado"
                })
            }

            resolve(payload.sub)
        } catch (err) {
            reject({
                status: 500,
                message: "Token invalido"
            })
        }
    })

    return decoded
}

module.exports = {
    createToken,
    decodeToken
}
