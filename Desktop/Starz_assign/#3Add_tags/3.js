const addTagButton = document.querySelector('.add-tag-button');
const tagsContainer = document.querySelector('.tags');

addTagButton.addEventListener('click', () => {
  const tagName = prompt('Enter tag name:');
  if (tagName) {
    const tag = document.createElement('span');
    tag.classList.add('tag');
    tag.textContent = tagName;
    tagsContainer.appendChild(tag);
  }
});
