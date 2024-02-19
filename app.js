const express = require('express');
const { Pool } = require('pg');

const app = express();

// Configuración de la conexión a la base de datos PostgreSQL
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'mirada_analitica',
  password: 'Ale123roblesmora',
  port: 5433,
});

// Ruta para obtener los datos de la base de datos y enviarlos al frontend
app.get('/', (req, res) => {
  pool.query('SELECT * FROM candidato', (err, result) => {
    if (err) {
      throw err;
    }
    res.send(result.rows);
  });
});

// Iniciar el servidor en el puerto 3000
app.listen(3000, () => {
  console.log('Servidor iniciado en el puerto 3000');
});
