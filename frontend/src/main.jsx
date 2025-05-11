import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import './globals.css' 
import { AuroraBackground } from './ui/aurora-background'  

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <AuroraBackground className="animate-aurora" />
  </React.StrictMode>
)
