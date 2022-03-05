require('dotenv').config()
const mongoose = require("mongoose")
const dbPort = 27017
const serverPort = 3000
const database = "greenhouse"

var app = require("./app")

process.on('uncaughtException', (error)  => {
  console.error(error);
})

process.on('unhandledRejection', (error, promise) => {
  console.error('Unhandled promise rejection: ', promise);
  console.error('Error: ', error );
});

// silence DeprecationWarning: collection.ensureIndex is deprecated. Use createIndexes instead.
mongoose.set('useCreateIndex', true)

mongoose
  .connect(`mongodb://localhost:${dbPort}/${database}`, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => {
    console.log(`Database corriendo en el puerto: ${dbPort}`)

    app.listen(serverPort, () => {
      console.log(`Servidor corriento en el puerto: ${serverPort}`)
    })
  })
  .catch((e) => console.error(e))
