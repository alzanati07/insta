const express = require('express');
const path = require('path');
const cors = require('cors'); // <-- استدعاء CORS
const { getStories } = require('../scraper/scraper');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors()); // <-- تفعيل CORS
app.use(express.static(path.join(__dirname, '../public')));

app.get('/api/stories/:username', async (req, res) => {
  const stories = await getStories(req.params.username);
  res.json(stories);
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
