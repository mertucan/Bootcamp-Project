import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PersonalizedProgram = ({ settings, scrollRef }) => { // scrollRef prop'unu al
    const [programData, setProgramData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Sadece 'settings' prop'u mevcutsa ve doluysa API isteği yap
        if (settings) {
            setLoading(true);
            setError(null);
            setProgramData(null);

            const fetchProgram = async () => {
                try {
                    // Backend API'sine POST isteği gönder
                    // Gövdede kullanıcının seçimlerini yolla
                    const response = await axios.post('http://localhost:5000/generate-program', settings);
                    setProgramData(response.data);
                } catch (err) {
                    setError('Program yüklenirken bir hata oluştu. API sunucusunun çalıştığından emin olun.');
                    console.error(err);
                } finally {
                    setLoading(false);
                }
            };

            fetchProgram();
        }
    }, [settings]); // 'settings' değiştiğinde bu effect tekrar çalışır

    // YENİ: Veri yüklendiğinde kaydırma animasyonunu tetikle
    useEffect(() => {
        if (programData && scrollRef.current) {
            setTimeout(() => {
                scrollRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
    }, [programData, scrollRef]); // programData değiştiğinde çalışır

    if (!settings) {
        return null; // Ayarlar yoksa hiçbir şey gösterme
    }

    if (loading) {
        return <div className="personalized-program-container"><p>Programınız oluşturuluyor...</p></div>;
    }

    if (error) {
        return <div className="personalized-program-container"><p className="error-message">{error}</p></div>;
    }

    if (!programData) {
        return null;
    }

    // Haftanın günlerini doğru sırada render etmek için bir dizi oluşturalım
    const weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    const scheduleKeys = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"];
    const schedule = programData.schedule || {};

    return (
        <div className="personalized-program-container">
            <h2>Your Personalized Program</h2>
            <div className="program-details rounded-lg border border-stone-200 dark:border-gray-700 bg-white dark:bg-gray-900 shadow-lg overflow-hidden p-6">
                <h3 className="text-2xl font-bold text-stone-800 dark:text-gray-200 mb-2">{programData.programName}</h3>
                <p className="text-stone-500 dark:text-gray-400 mb-6">{programData.description}</p>
                
                <div className="overflow-x-auto">
                    <table className="min-w-full border-collapse border border-stone-300 dark:border-gray-600">
                        <thead>
                            <tr>
                                {weekDays.map(day => (
                                    <th key={day} className="border border-stone-300 dark:border-gray-600 px-4 py-3 text-sm font-medium text-stone-900 dark:text-white bg-stone-50 dark:bg-gray-800 text-center">
                                        {day}
                                    </th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                {scheduleKeys.map(dayKey => (
                                    <td key={dayKey} className="border border-stone-300 dark:border-gray-600 px-4 py-4 text-sm text-stone-600 dark:text-gray-300 bg-white dark:bg-gray-900 align-top h-48">
                                        <ul className="space-y-2">
                                            {(schedule[dayKey] || []).map((exercise, index) => (
                                                <li key={index}>
                                                    <strong>{exercise.name}</strong>
                                                    {exercise.sets && <span className="block text-xs">{exercise.sets}</span>}
                                                </li>
                                            ))}
                                        </ul>
                                    </td>
                                ))}
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default PersonalizedProgram;
