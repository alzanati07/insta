const express = require('express');
const cors = require('cors'); // ✅ استدعاء مكتبة CORS
const path = require('path');
const { getStories } = require('../scraper/scraper');

const app = express();
const PORT = process.env.PORT || 3000;

// ✅ تفعيل CORS لجميع الطلبات
app.use(cors());

// تقديم الملفات الثابتة من مجلد public
app.use(express.static(path.join(__dirname, '../public')));

// مسار API لجلب القصص
app.get('/api/stories/:username', async (req, res) => {
  try {
    const stories = await getStories(req.params.username);
    res.json(stories);
  } catch (error) {
    console.error('Error fetching stories:', error);
    res.status(500).json({ error: 'Failed to fetch stories' });
  }
});

// تشغيل السيرفر
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
