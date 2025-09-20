import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';


const MyActivity = () => {
    const [analysis, setAnalysis] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAnalysis = async () => {
            // This data would normally come from the logged-in user or a form
            const sampleUserData = {
                "TotalSteps": 8560, "TotalDistance": 6.1, "VeryActiveMinutes": 35,
                "FairlyActiveMinutes": 30, "LightlyActiveMinutes": 210,
                "SedentaryMinutes": 550, "Calories": 2450
            };
            try {
                const response = await axios.post('http://localhost:5000/activity-analysis', sampleUserData);
                setAnalysis(response.data);
            } catch (err) {
                setError('Could not load activity analysis. Please ensure the API server is running.');
            } finally {
                setLoading(false);
            }
        };
        fetchAnalysis();
    }, []);

    if (loading) return <p className="text-center text-gray-300">Loading your activity analysis...</p>;
    if (error) return <p className="text-center text-red-500">{error}</p>;
    if (!analysis) return <p className="text-center text-gray-300">No analysis data available.</p>;

    const { userData, predictedLevel, modelAccuracy, classificationReport, sleepData, stressScore } = analysis;

    const activityData = [
        { name: 'Very Active', minutes: userData.VeryActiveMinutes, fill: '#ef4444' },
        { name: 'Fairly Active', minutes: userData.FairlyActiveMinutes, fill: '#f97316' },
        { name: 'Lightly Active', minutes: userData.LightlyActiveMinutes, fill: '#84cc16' },
        { name: 'Sedentary', minutes: userData.SedentaryMinutes, fill: '#277dF5' },
    ];
    
    // --- YENİ BİLEŞENLER ---

    const TooltipInfo = ({ text }) => (
        <div className="group relative flex justify-center">
            <span className="material-symbols-outlined ml-2 cursor-help text-base text-gray-400 dark:text-gray-500">help</span>
            <span className="absolute bottom-full z-10 mb-2 w-64 scale-0 rounded bg-gray-800 p-3 text-center text-xs text-white transition-all group-hover:scale-100">{text}</span>
        </div>
    );

    const StatCard = ({ title, value, tooltipText }) => (
        <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md flex flex-col justify-between">
            <h3 className="text-lg font-semibold text-stone-500 dark:text-gray-400 flex items-center justify-center">
                {title}
                <TooltipInfo text={tooltipText} />
            </h3>
            <p className="text-4xl font-bold text-stone-800 dark:text-gray-200 mt-2">{value}</p>
        </div>
    );

    const GoalChart = ({ value, goal, title, unit, color }) => {
        const percentage = Math.round((value / goal) * 100);
        return (
            <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md flex flex-col items-center">
                <h3 className="text-xl font-bold text-stone-800 dark:text-gray-200 mb-4">{title}</h3>
                <div style={{ width: '150px', height: '150px' }}>
                    <CircularProgressbar
                        value={percentage}
                        text={`${percentage}%`}
                        styles={buildStyles({
                            pathColor: color,
                            textColor: '#f1f5f9',
                            trailColor: '#374151',
                        })}
                    />
                </div>
                <p className="mt-4 text-stone-500 dark:text-gray-400">
                    Goal: {goal.toLocaleString()} {unit} | Completed: {value.toLocaleString()} {unit}
                </p>
            </div>
        );
    };
    
    const InfoSection = ({ title, children }) => (
        <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
            <h3 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-4">{title}</h3>
            <div className="text-stone-600 dark:text-gray-300 space-y-2">
                {children}
            </div>
        </div>
    );


    return (
        <div className="space-y-12">
            <div className="text-center">
                <h1 className="text-4xl font-extrabold tracking-tighter text-stone-900 dark:text-white">My Comprehensive Activity Analysis</h1>
                <p className="text-stone-500 dark:text-gray-400 text-lg mt-4 max-w-3xl mx-auto">
                    A deep dive into your health and fitness metrics, powered by our AI model.
                </p>
            </div>
            
            <InfoSection title="How Is Your Fitness Level Determined?">
                <p>
                    Our AI model analyzes your daily activity data (like total steps, distance covered, active minutes at different intensities, and calories burned). It compares this data with anonymized data from thousands of users in a large dataset. By grouping you with users who have similar activity profiles, it determines that <strong>{predictedLevel}</strong> is the level that best reflects your current fitness status. This helps us recommend the most suitable workout program for you.
                </p>
            </InfoSection>

            {/* New Score Cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 text-center">
                <StatCard title="Predicted Fitness Level" value={predictedLevel} tooltipText="Your overall fitness level as predicted by the AI based on your daily activity metrics." />
                <StatCard title="Sleep Quality Score" value={`${sleepData.quality_score} / 100`} tooltipText="Calculated based on your sleep efficiency (the ratio of time asleep to time in bed). A higher score indicates more restful sleep." />
                <StatCard title="Estimated Stress Score" value={`${stressScore} / 100`} tooltipText="Estimated based on your heart rate variability. A lower score could potentially indicate a higher level of stress. (This is a reference value)." />
                <StatCard title="Model Accuracy" value={`${(modelAccuracy * 100).toPrecision(4)}%`} tooltipText="This score represents the overall accuracy of our model that predicts your fitness level. It is calculated using 5-fold Cross-Validation."/>
            </div>
            
            {/* Goal Charts */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <GoalChart value={userData.TotalSteps} goal={10000} title="Daily Step Goal" unit="steps" color="#ef4444" />
                <GoalChart value={sleepData.total_minutes_asleep} goal={480} title="Daily Sleep Goal" unit="minutes" color="#3b82f6" />
            </div>

            {/* Existing Charts */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 activity-charts">
                <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
                    <h3 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-6 text-center">Daily Active Minutes</h3>
                    <ResponsiveContainer width="100%" height={300}>
                        <BarChart data={activityData}>
                            <CartesianGrid strokeDasharray="3 3" className="stroke-stone-200 dark:stroke-gray-700" />
                            <XAxis dataKey="name" />
                            <YAxis />
                            <Tooltip />
                            <Legend wrapperStyle={{ color: '#f1f5f9' }} />
                            <Bar dataKey="minutes" name="Minutes per Day">
                                {activityData.map((entry, index) => <Cell key={`cell-${index}`} fill={entry.fill} />)}
                            </Bar>
                        </BarChart>
                    </ResponsiveContainer>
                </div>
                <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
                    <h3 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-6 text-center">Activity Distribution</h3>
                     <ResponsiveContainer width="100%" height={300}>
                        <PieChart>
                            <Pie data={activityData} dataKey="minutes" nameKey="name" cx="50%" cy="50%" outerRadius={100} label>
                                {activityData.map((entry, index) => <Cell key={`cell-${index}`} fill={entry.fill} />)}
                            </Pie>
                            <Tooltip />
                            <Legend wrapperStyle={{ color: '#f1f5f9' }} />
                        </PieChart>
                    </ResponsiveContainer>
                </div>
            </div>

            {/* Model Performance Table */}
            <InfoSection title="Model Performance Details">
                <p className="text-center mb-4">This table details how successful our fitness level prediction model is for each class.</p>
                <div className="overflow-x-auto">
                    <table className="min-w-full text-left text-sm">
                         <thead className="border-b dark:border-gray-700">
                             <tr>
                                 <th className="p-2 text-stone-800 dark:text-gray-200">Class</th>
                                 <th className="p-2 text-stone-800 dark:text-gray-200">Precision</th>
                                 <th className="p-2 text-stone-800 dark:text-gray-200">Recall</th>
                                 <th className="p-2 text-stone-800 dark:text-gray-200">F1-Score</th>
                                 <th className="p-2 text-stone-800 dark:text-gray-200">Support</th>
                             </tr>
                         </thead>
                         <tbody>
                            {(classificationReport ? Object.entries(classificationReport).filter(([key]) => !['accuracy', 'macro avg', 'weighted avg'].includes(key)) : []).map(([className, metrics]) => (
                                 <tr key={className} className="border-b dark:border-gray-700 text-stone-600 dark:text-gray-300">
                                     <td className="p-2 font-semibold">{className}</td>
                                     <td className="p-2">{metrics.precision.toPrecision(3)}</td>
                                     <td className="p-2">{metrics.recall.toPrecision(3)}</td>
                                     <td className="p-2">{metrics['f1-score'].toPrecision(3)}</td>
                                     <td className="p-2">{metrics.support}</td>
                                 </tr>
                             ))}
                         </tbody>
                     </table>
                 </div>
            </InfoSection>
        </div>
    );
};

export default MyActivity;
