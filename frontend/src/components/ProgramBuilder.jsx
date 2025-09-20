import { useState, useEffect, useMemo } from 'react';
import axios from 'axios';

// Adım durumunu yöneten yardımcı bileşen
const Step = ({ number, title, active, completed }) => (
    <li className="relative pr-8 sm:pr-20 flex-1">
        <div className="flex items-center">
            <span className={`relative z-10 flex items-center justify-center w-10 h-10 rounded-full font-bold transition-colors duration-500 ${
                active || completed ? 'bg-red-600 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-500 dark:text-gray-400'
            }`}>
                {number}
            </span>
            {/* Arka plandaki tam genişlikte çizgi */}
            <div aria-hidden="true" className={`absolute inset-0 top-5 left-5 -ml-px h-0.5 w-full bg-gray-200 dark:bg-gray-700`}></div>
            {/* Tamamlandığında görünen renkli çizgi */}
            <div aria-hidden="true" className={`absolute inset-0 top-5 left-5 -ml-px h-0.5 w-full bg-red-600 transition-all duration-500 ${ completed ? 'scale-x-100' : 'scale-x-0' }`} style={{ transformOrigin: 'left' }}></div>
        </div>
        <div className="mt-3 absolute" style={{ left: '1.25rem', transform: 'translateX(-50%)' }}>
            <span className={`block font-semibold text-center w-24 transition-colors duration-500 ${
                active || completed ? 'text-red-500 dark:text-red-400' : 'text-gray-500 dark:text-gray-400'
            }`}>
                {title}
            </span>
        </div>
    </li>
);


function ProgramBuilder({ onGenerateProgram, onReset }) {
  const initialSelections = {
    goal: '',
    level: '',
    frequency: '',
  };
  const [selections, setSelections] = useState(initialSelections);
  const [predictedLevel, setPredictedLevel] = useState(null);
  const [isLevelLoading, setLevelLoading] = useState(true);

  useEffect(() => {
    const predictUserLevel = async () => {
        const sampleUserData = {
            "TotalSteps": 7500, "TotalDistance": 5.5, "VeryActiveMinutes": 20,
            "FairlyActiveMinutes": 25, "LightlyActiveMinutes": 190,
            "SedentaryMinutes": 600, "Calories": 2100
        };
        try {
            const response = await axios.post('http://localhost:5000/predict-level', sampleUserData);
            const level = response.data.predictedLevel;
            if (level) {
                setSelections(prev => ({ ...prev, level: level }));
                setPredictedLevel(level);
            }
        } catch (error) {
            console.error("Error predicting user level:", error);
        } finally {
            setLevelLoading(false);
        }
    };
    predictUserLevel();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setSelections(prev => ({ ...prev, [name]: value }));
  };
  
  const handleReset = () => {
      if (onReset) {
        onReset(); // Üst bileşene tabloyu temizlemesini söyle
      }

      if (currentStep === 3) {
          // Adım 3'ten Adım 2'ye animasyonlu geçiş
          setSelections(prev => ({ ...prev, frequency: '' }));

          // Adım 2'den Adım 1'e geçiş için gecikme
          setTimeout(() => {
              setSelections({
                  ...initialSelections,
                  level: predictedLevel || ''
              });
          }, 500); // CSS animasyon süresiyle eşleşmeli
      } else {
          // Adım 2 veya 1'deyse, direkt sıfırla
          setSelections({
              ...initialSelections,
              level: predictedLevel || ''
          });
      }
  }

  const currentStep = useMemo(() => {
    const goalSelected = selections.goal !== '';
    const frequencySelected = selections.frequency !== '';
    const levelSelected = selections.level !== '';

    // Program oluşturmaya hazır
    if (goalSelected && frequencySelected && levelSelected) {
        return 3;
    }

    // Kullanıcı manuel bir seçim yaptığında ilerle (AI'nın seçimini yoksay)
    if (goalSelected || frequencySelected) {
        return 2;
    }

    // Başlangıç durumu
    return 1;
  }, [selections]);

  const isFormComplete = currentStep === 3;

  const handleGenerateClick = () => {
    if (isFormComplete) {
      onGenerateProgram({ ...selections, predictedLevel });
    }
  };

  return (
    <div className="max-w-4xl w-full mx-auto">
      <div className="text-center">
        <h2 className="text-4xl sm:text-5xl font-extrabold tracking-tight text-stone-900 dark:text-white">Build Your Own Fitness Program</h2>
        <p className="mt-4 max-w-3xl mx-auto text-lg text-gray-500 dark:text-gray-400">
            Follow the steps below to create a personalized fitness program. Your fitness level is automatically detected by our AI based on your{' '}
            <a href="https://www.kaggle.com/datasets/arashnic/fitbit" target="_blank" rel="noopener noreferrer" className="text-red-500 hover:underline font-medium">
                Fitbit data
            </a>
            , but you can override it if you wish.
        </p>
      </div>

      <div className="mt-12 mb-16">
        <nav aria-label="Progress">
            <ol className="flex items-center" role="list">
                <Step number={1} title="Define Goals" active={currentStep === 1} completed={currentStep > 1} />
                <Step number={2} title="Choose Preferences" active={currentStep === 2} completed={currentStep > 2} />
                <li className="relative flex-shrink-0">
                    <div className="flex items-center">
                         <span className={`flex items-center justify-center w-10 h-10 rounded-full font-bold transition-colors duration-500 ${
                            currentStep === 3 ? 'bg-red-600 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-500 dark:text-gray-400'
                         }`}>3</span>
                    </div>
                     <div className="mt-3 absolute" style={{ left: '1.25rem', transform: 'translateX(-50%)' }}>
                         <span className={`block font-semibold text-center w-32 transition-colors duration-500 ${
                            currentStep === 3 ? 'text-red-500 dark:text-red-400' : 'text-gray-500 dark:text-gray-400'
                         }`}>Generate Program</span>
                    </div>
                </li>
            </ol>
        </nav>
      </div>
      
      <div className="mt-12 bg-white dark:bg-gray-800 p-8 rounded-lg shadow-lg">
          <div className="space-y-8">
            {/* Sıra 1: Hedef ve Frekans */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-6">
                <div>
                  <label htmlFor="goal" className="block text-sm font-medium text-gray-600 dark:text-gray-300 mb-1">Your Fitness Goal</label>
                  <select id="goal" name="goal" value={selections.goal} onChange={handleChange} className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-700 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                    <option value="">Select an option...</option>
                    <option value="muscle_gain">Muscle Gain</option>
                    <option value="weight_loss">Weight Loss</option>
                    <option value="strength">Strength</option>
                    <option value="general_health">General Health</option>
                  </select>
                </div>
                <div>
                  <label htmlFor="frequency" className="block text-sm font-medium text-gray-600 dark:text-gray-300 mb-1">Exercise Frequency (Per Week)</label>
                  <select id="frequency" name="frequency" value={selections.frequency} onChange={handleChange} className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-700 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                    <option value="">Select an option...</option>
                    <option value="3">3 Days</option>
                    <option value="4">4 Days</option>
                    <option value="5">5 Days</option>
                  </select>
                </div>
            </div>
            {/* Sıra 2: Seviye (Ortalanmış) */}
            <div className="flex justify-center">
                <div className="w-full md:w-1/2">
                  <label htmlFor="level" className="block text-sm font-medium text-gray-600 dark:text-gray-300 mb-1">Your Fitness Level</label>
                  <select id="level" name="level" value={selections.level} onChange={handleChange} disabled={isLevelLoading} className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-700 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500 disabled:opacity-50">
                    {isLevelLoading ? <option>Analyzing your activity...</option> : <>
                      <option value="">Select an option...</option>
                      <option value="beginner">Beginner</option>
                      <option value="intermediate">Intermediate</option>
                      <option value="advanced">Advanced</option>
                    </>}
                  </select>
                </div>
            </div>
          </div>
          <div className="mt-10 flex flex-col sm:flex-row-reverse items-center justify-center gap-4">
            <button onClick={handleGenerateClick} disabled={!isFormComplete} className="w-full sm:w-auto inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-red-600 hover:bg-red-700 disabled:bg-gray-400 disabled:cursor-not-allowed focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 dark:focus:ring-offset-gray-800 transition-transform transform hover:scale-105">
                Generate Program
            </button>
            <button onClick={handleReset} type="button" className="w-full sm:w-auto inline-flex items-center justify-center px-8 py-3 border border-stone-300 dark:border-gray-600 text-base font-medium rounded-md text-gray-600 dark:text-gray-300 bg-transparent hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 dark:focus:ring-offset-gray-800 transition-colors">
                Reset
            </button>
          </div>
      </div>
    </div>
  );
}

export default ProgramBuilder;
