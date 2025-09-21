import { useState, useRef, useEffect } from 'react';
import ProgramBuilder from '../components/ProgramBuilder';
import PersonalizedProgram from '../components/PersonalizedProgram';

const MainPage = () => {
  const [programSettings, setProgramSettings] = useState(null);
  const programRef = useRef(null);

  const handleGenerateProgram = (settings) => {
    setProgramSettings(settings);
  };

  const handleClearProgram = () => {
    setProgramSettings(null);
  };

  return (
    <>
      <ProgramBuilder onGenerateProgram={handleGenerateProgram} onReset={handleClearProgram} />
      {programSettings && (
        <div ref={programRef} className="mt-16">
          {/* scrollRef prop'u ile referansı çocuğa iletiyoruz */}
          <PersonalizedProgram settings={programSettings} scrollRef={programRef} />
        </div>
      )}
    </>
  );
};

export default MainPage;
