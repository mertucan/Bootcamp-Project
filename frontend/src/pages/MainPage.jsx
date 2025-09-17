import { useState, useRef, useEffect } from 'react';
import ProgramBuilder from '../components/ProgramBuilder';
import PersonalizedProgram from '../components/PersonalizedProgram';

const MainPage = () => {
  const [programSettings, setProgramSettings] = useState(null);
  const programRef = useRef(null);

  const handleGenerateProgram = (settings) => {
    setProgramSettings(settings);
  };

  useEffect(() => {
    if (programSettings && programRef.current) {
      setTimeout(() => {
        programRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 100);
    }
  }, [programSettings]);

  return (
    <>
      <ProgramBuilder onGenerateProgram={handleGenerateProgram} />
      {programSettings && (
        <div ref={programRef} className="mt-16">
          <PersonalizedProgram settings={programSettings} />
        </div>
      )}
    </>
  );
};

export default MainPage;
