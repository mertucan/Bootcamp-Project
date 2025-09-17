import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const MyActivity = () => {
    const [analysis, setAnalysis] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAnalysis = async () => {
            const sampleUserData = {
                "TotalSteps": 7500, "TotalDistance": 5.5, "VeryActiveMinutes": 20,
                "FairlyActiveMinutes": 25, "LightlyActiveMinutes": 190,
                "SedentaryMinutes": 600, "Calories": 2100
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

    if (loading) return <p className="text-center">Loading activity analysis...</p>;
    if (error) return <p className="text-center text-red-500">{error}</p>;
    if (!analysis) return <p className="text-center">No analysis data available.</p>;

    const { userData, predictedLevel, modelAccuracy, classificationReport } = analysis;

    const activityData = [
        { name: 'Very Active', minutes: userData.VeryActiveMinutes, fill: '#ef4444' }, // red-500
        { name: 'Fairly Active', minutes: userData.FairlyActiveMinutes, fill: '#f97316' }, // orange-500
        { name: 'Lightly Active', minutes: userData.LightlyActiveMinutes, fill: '#84cc16' }, // lime-500
        { name: 'Sedentary', minutes: userData.SedentaryMinutes, fill: '#6b7280' }, // gray-500
    ];

    const reportData = classificationReport ? Object.entries(classificationReport).filter(([key]) => !['accuracy', 'macro avg', 'weighted avg'].includes(key)) : [];

    const TooltipInfo = ({ text }) => (
        <div className="group relative flex justify-center">
            <span className="material-symbols-outlined ml-2 cursor-help text-base text-gray-400 dark:text-gray-500">
                help
            </span>
            <span className="absolute bottom-full mb-2 w-64 scale-0 rounded bg-gray-800 p-3 text-center text-xs text-white transition-all group-hover:scale-100">
                {text}
            </span>
        </div>
    );

    return (
        <div className="space-y-12">
            <div className="text-center">
                <h1 className="text-4xl font-extrabold tracking-tighter text-stone-900 dark:text-white">My Activity Analysis</h1>
                <p className="text-stone-500 dark:text-gray-400 text-lg mt-4 max-w-2xl mx-auto">
                    An overview of your activity levels based on our Machine Learning model.
                </p>
            </div>

            {/* Stat Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
                <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
                    <h3 className="text-lg font-semibold text-stone-500 dark:text-gray-400 flex items-center justify-center">
                        Predicted Fitness Level
                        <TooltipInfo text="This is the fitness level predicted by our Machine Learning model based on your activity data (steps, active minutes, etc.)." />
                    </h3>
                    <p className="text-3xl font-bold text-red-600 dark:text-red-500 mt-2">{predictedLevel}</p>
                </div>
                <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
                    <h3 className="text-lg font-semibold text-stone-500 dark:text-gray-400">Average Daily Calories</h3>
                    <p className="text-3xl font-bold text-stone-800 dark:text-gray-200 mt-2">{userData.Calories.toLocaleString()}</p>
                </div>
                <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
                    <h3 className="text-lg font-semibold text-stone-500 dark:text-gray-400 flex items-center justify-center">
                        Model Accuracy
                        <TooltipInfo text="This score represents the model's overall accuracy, calculated using a robust method called 5-fold Cross-Validation. It reflects how often the model's predictions are correct." />
                    </h3>
                    <p className="text-3xl font-bold text-stone-800 dark:text-gray-200 mt-2">{(modelAccuracy * 100).toPrecision(4)}%</p>
                </div>
            </div>

            {/* Charts Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 activity-charts">
                <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
                    <h3 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-6 text-center">Daily Active Minutes (Bar)</h3>
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
                    <h3 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-6 text-center">Activity Distribution (Pie)</h3>
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

            {/* Classification Report Table */}
            <div className="p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
                <h3 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-6 text-center flex items-center justify-center">
                    Model Performance Details
                    <TooltipInfo 
                        text={
                            <>
                            Precision: Of all the times the model predicted a level, how often was it right?<br /><br />
                            Recall: Of all the actual instances of a level, how many did the model correctly identify?<br /><br />
                            F1-Score: A combined measure of Precision and Recall.<br /><br />
                            Support: The number of actual occurrences of the class in the dataset.
                            </>
                        }
                        />
                </h3>
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
                            {reportData.map(([className, metrics]) => (
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
            </div>
        </div>
    );
};

export default MyActivity;
