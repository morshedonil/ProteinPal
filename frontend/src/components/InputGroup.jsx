import { InputText } from 'primereact/inputtext';
import { Button } from 'primereact/button';
import { useEffect, useRef, useState } from 'react';

function InputGroup() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const chatEndRef = useRef(null); // Reference to the bottom of the chat

  const handleSearch = () => {
    if (input.trim() === '') return;

    const userMsg = { sender: 'user', text: input };
    const botMsg = { sender: 'bot', text: 'Paad khaaa' };

    setMessages((prev) => [...prev, userMsg, botMsg]);
    setInput('');
  };

  // Scroll to bottom when messages update
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="chat-container">
      {/* Chat History */}
      <div className="chat-history">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={msg.sender === 'user' ? 'text' : 'text-bot'}
          >
            {msg.sender === 'user' ? 'You: ' : 'Bot: '}
            {msg.text}
          </div>
        ))}
        {/* Dummy div to scroll into view */}
        <div ref={chatEndRef} />
      </div>

      {/* Input box */}
      <div className="input-wrapper">
        <div className="input-container">
          <InputText
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter') {
                handleSearch();
              }
            }}
            placeholder="Enter your ingredients"
            className="custom-input"
          />
          <Button
            icon="pi pi-search"
            className="custom-icon-button"
            onClick={handleSearch}
          />
        </div>
      </div>
    </div>
  );
}

export default InputGroup;
