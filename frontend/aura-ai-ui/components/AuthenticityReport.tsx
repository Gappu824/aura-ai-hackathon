import React from 'react';

interface AuthenticityReportProps {
  analysis: {
    authenticity_score: number;
    // --- MODIFIED: Expecting 'reasoning' string now ---
    reasoning: string;
    // Added 'error' to the interface for robust error display from the backend
    error?: string;
  } | null;
  isLoading: boolean;
}

const AuthenticityReport: React.FC<AuthenticityReportProps> = ({ analysis, isLoading }) => {
  if (isLoading) {
    return <div className="text-sm text-gray-500 animate-pulse">Analyzing...</div>;
  }

  if (!analysis) return null;

  // --- ADDED: Handle error returned by backend ---
  if (analysis.error) {
    return (
      <div className="mt-4 p-3 bg-red-100 border border-red-300 rounded text-red-700 text-sm">
        Error: {analysis.error}
      </div>
    );
  }
  // --- END ADDED ---

  const scoreColor = analysis.authenticity_score > 0.7 ? 'text-green-600' : analysis.authenticity_score > 0.4 ? 'text-yellow-600' : 'text-red-600';

  return (
    <div className="p-3 mt-2 text-xs bg-gray-50 rounded-md border">
      <div className="font-bold">Authenticity Score: <span className={scoreColor}>{(analysis.authenticity_score * 100).toFixed(0)}%</span></div>
      {/* --- MODIFIED: Display the 'reasoning' string directly --- */}
      <p className="mt-2 text-gray-700">
        <strong>Reasoning:</strong> {analysis.reasoning}
      </p>
      {/* --- REMOVED: No longer expecting key_positive_signals or potential_concerns arrays --- */}
      {/*
      {analysis.potential_concerns.length > 0 && (
        <ul className="list-disc list-inside text-red-700">
          {analysis.potential_concerns.map((concern, index) => <li key={index}>{concern}</li>)}
        </ul>
      )}
      {analysis.key_positive_signals.length > 0 && (
        <ul className="list-disc list-inside text-green-700">
          {analysis.key_positive_signals.map((signal, index) => <li key={index}>{signal}</li>)}
        </ul>
      )}
      */}
    </div>
  );
};

export default AuthenticityReport;