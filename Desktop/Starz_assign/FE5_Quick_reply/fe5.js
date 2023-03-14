// Listen for message selection events
chatBox.onMessageSelected((message) => {
    // If the message has a quick reply option
    if (message.hasQuickReply) {
      // Display the quick reply options
      const quickReplyOptions = message.quickReplyOptions;
      quickReplyOptions.forEach((option) => {
        // Render the quick reply button for each option
        const button = document.createElement('button');
        button.innerText = option.text;
        button.addEventListener('click', () => {
          // Send the selected quick reply back to the chat
          chatBox.sendMessage(option.text);
        });
        quickReplyContainer.appendChild(button);
      });
      // Show the quick reply container
      quickReplyContainer.style.display = 'block';
    }
  });
  
  // Listen for message sent events
  chatBox.onMessageSent(() => {
    // Hide the quick reply container
    quickReplyContainer.style.display = 'none';
  });
  