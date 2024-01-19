const express = require('express');
const { Client } = require('pg');

const app = express();
const port = 3000;

const connectionData = {
    user: 'postgres',
    host: 'localhost',
    database: 'mirada_analitica',
    password: 'Ale123roblesmora',
    port: 5432,
};

const client = new Client(connectionData);

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.get('/getData', (req, res) => {
    let tableName = req.query.tableName || 'presidencia';
    let query = `SELECT * FROM analisis.${tableName}`;

    client.connect();
    client.query(query)
        .then(response => {
            res.json(response.rows);
            client.end();
        })
        .catch(err => {
            client.end();
            res.status(500).json({ error: 'Error al obtener datos desde la base de datos' });
        });
});

app.listen(port, () => {
    console.log(`Servidor web iniciado en http://localhost:${port}`);
});

