import React from 'react';

interface ClarityAlertProps {
  alertText: string | null;
  isLoading: boolean;
}

const ClarityAlert: React.FC<ClarityAlertProps> = ({ alertText, isLoading }) => {
  if (isLoading) {
    return <div className="p-4 bg-gray-100 rounded-lg animate-pulse">Loading Clarity Insights...</div>;
  }

  if (!alertText) {
    return null; // Don't render anything if there's no alert
  }

  return (
    <div className="p-4 mb-4 text-blue-800 bg-blue-100 border-l-4 border-blue-500 rounded-lg shadow-md">
      <h3 className="font-bold">💡 Aura AI Clarity Alert</h3>
      <p>{alertText}</p>
    </div>
  );
};

export default ClarityAlert;