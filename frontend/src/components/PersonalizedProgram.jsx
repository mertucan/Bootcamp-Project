function PersonalizedProgram() {
  const weeklyProgram = [
    { day: 'Monday', workout: 'Chest & Triceps' },
    { day: 'Tuesday', workout: 'Back & Biceps' },
    { day: 'Wednesday', workout: 'Rest' },
    { day: 'Thursday', workout: 'Legs & Shoulders' },
    { day: 'Friday', workout: 'Cardio & Abs' },
    { day: 'Saturday', workout: 'Rest' },
    { day: 'Sunday', workout: 'Rest' },
  ];

  return (
    <div className="grid grid-cols-1 lg:grid-cols-1 gap-12 items-start">
      <div className="space-y-8">
        <div className="text-center lg:text-left">
          <h1 className="text-5xl font-extrabold tracking-tighter text-stone-900 dark:text-white">
            Your Personalized Program
          </h1>
          <p className="text-stone-500 dark:text-gray-400 text-lg mt-4 max-w-xl mx-auto lg:mx-0">
            Below you can see your program tailored to your goals and preferences.
          </p>
        </div>
        <div className="rounded-lg border border-stone-200 dark:border-gray-700 bg-white dark:bg-gray-900 shadow-lg overflow-hidden">
          <div className="p-6">
            <h2 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-4">Weekly Training Plan</h2>
            <div className="overflow-x-auto">
              <table className="min-w-full border-collapse border border-stone-300 dark:border-gray-600">
                <tbody>
                  <tr>
                    {weeklyProgram.map((item) => (
                      <td key={`day-${item.day}`} className="border border-stone-300 dark:border-gray-600 px-4 py-4 text-sm font-medium text-stone-900 dark:text-white bg-stone-50 dark:bg-gray-800 text-center">
                        {item.day}
                      </td>
                    ))}
                  </tr>
                  <tr>
                    {weeklyProgram.map((item) => (
                      <td key={`workout-${item.day}`} className="border border-stone-300 dark:border-gray-600 px-4 py-4 text-sm text-stone-600 dark:text-gray-300 bg-white dark:bg-gray-900 text-center">
                        {item.workout}
                      </td>
                    ))}
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PersonalizedProgram;
