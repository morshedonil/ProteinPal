import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import 'primereact/resources/themes/lara-light-blue/theme.css';  // Theme (choose one)
import 'primereact/resources/primereact.min.css';               // Core CSS
import 'primeicons/primeicons.css';                             // Icons
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
