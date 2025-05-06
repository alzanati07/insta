async function getStories(username) {
  const stories = [
    { id: 1, image: 'https://placekitten.com/400/600' },
    { id: 2, image: 'https://placekitten.com/401/601' }
  ];
  return stories;
}

module.exports = { getStories };