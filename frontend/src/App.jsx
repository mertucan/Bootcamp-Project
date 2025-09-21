import { Routes, Route, useLocation } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import MainPage from './pages/MainPage';
import MyActivity from './pages/MyActivity';

function App() {

  return (
    <div 
      className="relative flex h-auto min-h-screen w-full flex-col group/design-root overflow-x-hidden bg-[var(--background-color)] dark:bg-gray-900" 
      style={{
        "--select-button-svg": "url('data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%2724px%27 height=%2724px%27 fill=%27rgb(154,76,76)%27 viewBox=%270 0 256 256%27%3e%3cpath d=%27M181.66,170.34a8,8,0,0,1,0,11.32l-48,48a8,8,0,0,1-11.32,0l-48-48a8,8,0,0,1,11.32-11.32L128,212.69l42.34-42.35A8,8,0,0,1,181.66,170.34Zm-96-84.68L128,43.31l42.34,42.35a8,8,0,0,11.32-11.32l-48-48a8,8,0,0,0-11.32,0l-48,48A8,8,0,0,0,85.66,85.66Z%27%3e%3c/path%3e%3c/svg%3e')",
        fontFamily: 'Lexend, "Noto Sans", sans-serif'
      }}
    >
      <div className="layout-container flex h-full grow flex-col">
        <Header />
        
        <main className="flex-1 px-20 py-12">
          <div className="layout-content-container flex flex-col w-full mx-auto">
            <Routes>
              <Route path="/" element={<MainPage />} />
              <Route path="/my-activity" element={<MyActivity />} />
            </Routes>
          </div>
        </main>
        
        <Footer />
      </div>
    </div>
  );
}

export default App;