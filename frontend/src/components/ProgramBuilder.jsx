function ProgramBuilder({ onGenerateProgram }) {
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
                <select className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                  <option>Select an option...</option>
                  <option>Weight Loss</option>
                  <option>Muscle Gain</option>
                  <option>General Health</option>
                </select>
              </label>
              <label className="flex flex-col">
                <span className="text-sm font-medium text-stone-600 dark:text-gray-300 mb-1.5">Your Fitness Level</span>
                <select className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                  <option>Select an option...</option>
                  <option>Beginner</option>
                  <option>Intermediate</option>
                  <option>Advanced</option>
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
                <select className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                  <option>Select an option...</option>
                  <option>1-2 Days</option>
                  <option>3-4 Days</option>
                  <option>5-6 Days</option>
                </select>
              </label>
              <label className="flex flex-col">
                <span className="text-sm font-medium text-stone-600 dark:text-gray-300 mb-1.5">Exercise Duration (Minutes)</span>
                <select className="form-select w-full rounded-md border-stone-300 dark:border-gray-600 bg-stone-50 dark:bg-gray-800 text-stone-900 dark:text-gray-200 h-12 px-4 focus:border-red-500 focus:ring-red-500">
                  <option>Select an option...</option>
                  <option>15-30</option>
                  <option>30-45</option>
                  <option>45-60</option>
                  <option>60+</option>
                </select>
              </label>
            </div>
          </div>
        </div>
      </div>
      
      <div className="flex mt-12 justify-center">
        <button 
          onClick={onGenerateProgram}
          className="flex min-w-[200px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-md h-14 px-8 bg-red-600 text-white text-lg font-bold leading-normal tracking-wide hover:bg-red-700 transition-colors shadow-lg hover:shadow-xl"
        >
          <span className="truncate">Generate Program</span>
        </button>
      </div>
    </div>
  );
}

export default ProgramBuilder;
