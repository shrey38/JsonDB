const otherMessagesButton = document.querySelector('.other-messages-button');
const greetingMessageButton = document.querySelector('.greeting-message-button');
const awayMessageButton = document.querySelector('.away-message-button');
const quickMessageButton = document.querySelector('.quick-message-button');
const messagePage = document.querySelector('.message-page');
const customMessageInput = document.querySelector('.custom-message-input');
const saveMessageButton = document.querySelector('.save-message-button');
const templates = {
  greeting: "Hello! Thank you for contacting us. How may we assist you today?",
  away: "Sorry, we are currently away. Please leave a message and we will get back to you as soon as possible.",
  quick: "Sure, we can do that. When would you like it done?"
};
const characterLimit = 280; // Adjust as needed
const savedMessages = [];

// Helper function to truncate messages to character limit
function truncateMessage(message) {
  return message.length > characterLimit ? message.slice(0, characterLimit) : message;
}

// Populate message input with selected template
function populateMessageInput(template) {
  customMessageInput.value = template;
}

// Add new message to saved messages list
function addSavedMessage(message) {
  savedMessages.push(message);
  const savedMessagesList = document.querySelector('.saved-messages-list');
  const listItem = document.createElement('li');
  listItem.textContent = message;
  savedMessagesList.appendChild(listItem);
}

otherMessagesButton.addEventListener('click', () => {
  const otherMessagesPage = document.querySelector('.other-messages-page');
  otherMessagesPage.style.display = 'block';
});

greetingMessageButton.addEventListener('click', () => {
  messagePage.style.display = 'block';
  messagePage.querySelector('h2').textContent = 'Create a Greeting Message:';
  populateMessageInput(templates.greeting);
});

awayMessageButton.addEventListener('click', () => {
  messagePage.style.display = 'block';
  messagePage.querySelector('h2').textContent = 'Create an Away Message:';
  populateMessageInput(templates.away);
});

quickMessageButton.addEventListener('click', () => {
  messagePage.style.display = 'block';
  messagePage.querySelector('h2').textContent = 'Create a Quick Message:';
  populateMessageInput(templates.quick);
});

saveMessageButton.addEventListener('click', () => {
  const messageInput = document.querySelector('.message-input');
  const customMessage = truncateMessage(customMessageInput.value);
  messageInput.value = customMessage;
  messagePage.style.display = 'none';
  addSavedMessage(customMessage);
});
