const mongoose = require('mongoose');
const dbPort = 27017;
const serverPort = 3000;
const database = "facturas_db"

var app = require('./app')

mongoose.connect(`mongodb://localhost:${dbPort}/${database}`, {useNewUrlParser: true, useUnifiedTopology: true}, () => {
    console.log(`Database corriendo en el puerto: ${dbPort}`);

    app.listen(serverPort, () => {
        console.log(`Servidor corriento en el puerto: ${serverPort}`);
    });
});