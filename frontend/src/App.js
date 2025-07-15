import React, { useEffect, useState } from 'react';
import { Button, Container, Typography, List, ListItem } from '@mui/material';

function App() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws');
    ws.onmessage = (event) => {
      setMessages((prev) => [...prev, event.data]);
    };
    return () => ws.close();
  }, []);

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Binance Alerts (Demo)
      </Typography>
      <List>
        {messages.map((m, i) => (
          <ListItem key={i}>{m}</ListItem>
        ))}
      </List>
      <Button variant="contained">Connect</Button>
    </Container>
  );
}

export default App;
