import { useState, useEffect } from 'react';
import axios from 'axios';

function ProgramBuilder({ onGenerateProgram }) {
  const [selections, setSelections] = useState({
    goal: '',
    level: '',
    frequency: '',
    duration: ''
  });
  const [isLevelLoading, setLevelLoading] = useState(true);

  useEffect(() => {
    // Component yüklendiğinde kullanıcının seviyesini tahmin et
    const predictUserLevel = async () => {
        // Bu veriler, gerçek bir uygulamada kullanıcının Fitbit hesabından
        // veya benzeri bir kaynaktan gelmelidir.
        const sampleUserData = {
            "TotalSteps": 7500,
            "TotalDistance": 5.5,
            "VeryActiveMinutes": 20,
            "FairlyActiveMinutes": 25,
            "LightlyActiveMinutes": 190,
            "SedentaryMinutes": 600,
            "Calories": 2100
        };

        try {
            const response = await axios.post('http://localhost:5000/predict-level', sampleUserData);
            const predictedLevel = response.data.predictedLevel;
            if (predictedLevel) {
                // Tahmin edilen seviyeyi state'e ata
                setSelections(prev => ({ ...prev, level: predictedLevel }));
            }
        } catch (error) {
            console.error("Error predicting user level:", error);
            // Hata durumunda varsayılan olarak bir şey seçilmesin diye boş bırakabiliriz.
        } finally {
            setLevelLoading(false);
        }
    };
    predictUserLevel();
  }, []); // Boş dependency array, sadece component mount edildiğinde çalışmasını sağlar

  const handleChange = (e) => {
    const { name, value } = e.target;
    setSelections(prev => ({ ...prev, [name]: value }));
  };

  const isFormComplete = Object.values(selections).every(value => value !== '');

  const handleGenerateClick = () => {
    if (isFormComplete) {
      onGenerateProgram(selections);
    }
  };

  return (
    <div className="border-b border-stone-200 dark:border-gray-700 mb-16 pb-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-extrabold tracking-tighter text-stone-900 dark:text-white">
          Build Your Own Fitness Program
        </h1>
        <p className="text-stone-500 dark:text-gray-400 text-lg mt-4 max-w-2xl mx-auto">
          Follow the steps below to create a personalized fitness program tailored to your goals and preferences.
        </p>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-start max-w-4xl mx-auto">
        <div className="space-y-8">
          <div>
            <h2 className="text-2xl font-bold tracking-tight text-stone-900 dark:text-white mb-4">
              Step 1: Define Your Goals
            </h2>
            <div className="space-y-4">
              <label className="flex flex-col">
                <span className="text-sm font-medium text-stone-600 dark:text-gray-300 mb-1.5">Your Fitness Goal</span>
                <select name="goal" value={selections.goal} onChange={handleChange} className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                  <option value="">Select an option...</option>
                  <option value="muscle_gain">Muscle Gain</option>
                  <option value="weight_loss">Weight Loss</option>
                  <option value="strength">Strength</option>
                  <option value="general_health">General Health</option>
                </select>
              </label>
              <label className="flex flex-col">
                <span className="text-sm font-medium text-stone-600 dark:text-gray-300 mb-1.5">Your Fitness Level</span>
                <select name="level" value={selections.level} onChange={handleChange} disabled={isLevelLoading} className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500 disabled:opacity-50">
                  {isLevelLoading ? (
                    <option>Analyzing your activity...</option>
                  ) : (
                    <>
                      <option value="">Select an option...</option>
                      <option value="beginner">Beginner</option>
                      <option value="intermediate">Intermediate</option>
                      <option value="advanced">Advanced</option>
                    </>
                  )}
                </select>
              </label>
            </div>
          </div>
        </div>
        
        <div className="space-y-8">
          <div>
            <h2 className="text-2xl font-bold tracking-tight text-stone-900 dark:text-white mb-4">
              Step 2: Choose Your Preferences
            </h2>
            <div className="space-y-4">
              <label className="flex flex-col">
                <span className="text-sm font-medium text-stone-600 dark:text-gray-300 mb-1.5">Exercise Frequency (Per Week)</span>
                <select name="frequency" value={selections.frequency} onChange={handleChange} className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                  <option value="">Select an option...</option>
                  <option value="3">3 Days</option>
                  <option value="4">4 Days</option>
                  <option value="5">5 Days</option>
                </select>
              </label>
              <label className="flex flex-col">
                <span className="text-sm font-medium text-stone-600 dark:text-gray-300 mb-1.5">Exercise Duration (Minutes)</span>
                <select name="duration" value={selections.duration} onChange={handleChange} className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                  <option value="">Select an option...</option>
                  <option value="30">~30 Minutes</option>
                  <option value="45">~45 Minutes</option>
                  <option value="60">~60 Minutes</option>
                </select>
              </label>
            </div>
          </div>
        </div>
      </div>
      
      <div className="flex mt-12 justify-center">
        <button 
          onClick={handleGenerateClick}
          disabled={!isFormComplete}
          className="flex min-w-[200px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-md h-14 px-8 bg-red-600 text-white text-lg font-bold leading-normal tracking-wide hover:bg-red-700 transition-colors shadow-lg hover:shadow-xl disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          <span className="truncate">Generate Program</span>
        </button>
      </div>
    </div>
  );
}

export default ProgramBuilder;
