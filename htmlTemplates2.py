css = '''
<style>
  .chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start; /* Align items at the start */
  }

  .chat-message.user {
    background-color: #4a90e2; /* A blue color for user messages */
    color: #fff; /* Text color for user messages */
  }

  .chat-message.bot {
    background-color: #001f3f; /* A green color for bot messages */
    color: #fff; /* Text color for bot messages */
  }

  .chat-message .avatar {
    width: 20%;
    margin-right: 1rem; /* Add right margin for spacing */
  }

  .chat-message .avatar img {
    max-width: 100%;
    border-radius: 50%;
    object-fit: cover;
  }

  .chat-message .message {
    width: 80%;
    padding: 1rem; /* Improved padding for better readability */
  }
</style>
'''
bot_template = '''
<div class="chat-message bot">
  <div class="avatar">
    <img src="https://i.ibb.co/RyRh5P9/Screenshot-2023-11-17-at-3-15-16-PM.png">
  </div>
  <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
  <div class="avatar">
    <img src="https://i.ibb.co/W67yL7G/Screenshot-2023-11-17-at-3-27-50-PM.png">
  </div>
  <div class="message">{{MSG}}</div>
</div>
'''
