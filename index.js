const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Endpoint para comparar huellas
app.post('/compare', async (req, res) => {
    const { firstFeatureSet, secondFeatureSet } = req.body;
    if (!firstFeatureSet || !secondFeatureSet) {
        return res.status(400).json({ error: 'Faltan datos de huellas' });
    }

    try {
        // Llama al microservicio Python con SourceAFIS
        const response = await axios.post('http://localhost:5001/compare', {
            firstFeatureSet,
            secondFeatureSet
        });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Error al comparar huellas', details: error.message });
    }
});

app.listen(3001, () => {
    console.log('Servidor Node.js escuchando en puerto 3001');
});