const express = require('express');
const cors = require('cors');
const app = express();

const PORT = 8080;

app.use(cors());

app.get('/api/data', (req, res) => {
  res.send('Hello from Backend!');
});

app.get(
  '/api/azubi', (req, res) => {
    res.send("welcome to the azubi page")
  }
)

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
