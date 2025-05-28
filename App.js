import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; 
import Homepage from './components/assets/homepage/homepage'; 
import Registerpage from './components/assets/registerpage/registerpage'; 
import Assistant from './components/assets/assistant/assistant'; 
import Livestream from './components/assets/livestream/livestream'; 
import DatabasePage from './components/assets/databasepage/databasepage';

function App() {
    return (
        <Router>
            <Routes> 
                <Route path="/" element={<Homepage />} /> 
                <Route path="/registerpage" element={<Registerpage />} /> 
                <Route path="/databasepage" element={<DatabasePage />} />
                <Route path="/livestream" element={<Livestream />} /> 
                <Route path="/assistant" element={<Assistant />} /> 


            </Routes>
        </Router>
    );
}

export default App;
