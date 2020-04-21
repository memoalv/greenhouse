 'use strict'

 //Cargar modulos de node para crear server.
var express = require('express');
var bodyParser = require('body-parser');

 //Ejecutar express.
var app = express();


 //Cargar ficheros rutas.
 var routes = require('./routes/index')

 //Middlewares.
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

 //CORS.

 //Aniadir prefijos rutas / Cargar rutas.
 app.use('/', routes);

 //Exportar modulo(fichero actual).
 module.exports = app;