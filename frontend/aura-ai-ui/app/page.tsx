'use client';

import React, { useState, useEffect } from 'react';
import ClarityAlert from '../components/ClarityAlert';
import AuthenticityReport from '../components/AuthenticityReport';

// Mock data representing reviews for a product
const MOCK_REVIEWS = [
  "The shirt looks great, but I had to return it. I'm usually a Large, but this ran really small.",
  "Warning: runs small! I'd recommend sizing up at least one size.",
  "Love the color! Fabric is a bit thin. Sizing is way off, definitely runs small.",
  "Perfect fit and great quality. Not sure what others are talking about.",
  "Had to send it back, it was too tight. Order a size up.",
];

const MOCK_SINGLE_REVIEW_GOOD = "I've been using this for about two weeks now. It was easy to assemble, taking me about 15 minutes with the included tool. The material feels sturdy and has held up well to daily use. Specifically, I love the side pocket feature, which is perfect for my remote control.";

const MOCK_SINGLE_REVIEW_FAKE = "Wow. This product is amazing. I love it very much. Best purchase ever. Highly recommend to everyone. Five stars.";


export default function ProductPage() {
  const [clarityAlert, setClarityAlert] = useState<string | null>(null);
  const [isClarityLoading, setIsClarityLoading] = useState<boolean>(true);

  interface AnalysisResult {
    authenticity_score: number;
    reasoning: string;
    error?: string;
  }

  const [goodReviewAnalysis, setGoodReviewAnalysis] = useState<AnalysisResult | null>(null);
  const [isGoodReviewLoading, setIsGoodReviewLoading] = useState<boolean>(false);

  const [fakeReviewAnalysis, setFakeReviewAnalysis] = useState<AnalysisResult | null>(null);
  const [isFakeReviewLoading, setIsFakeReviewLoading] = useState<boolean>(false);

  const [userInputReview, setUserInputReview] = useState<string>('');
  const [userInputAuthenticityAnalysis, setUserInputAuthenticityAnalysis] = useState<AnalysisResult | null>(null);
  const [isUserInputAuthenticityLoading, setIsUserInputAuthenticityLoading] = useState<boolean>(false);
  const [userInputClarityAlert, setUserInputClarityAlert] = useState<string | null>(null);
  const [isUserInputClarityLoading, setIsUserInputClarityLoading] = useState<boolean>(false);
  const [apiError, setApiError] = useState<string | null>(null);


  useEffect(() => {
    const fetchClarityAlert = async () => {
      // Ensure the environment variable is available before fetching
      if (!process.env.NEXT_PUBLIC_API_URL) {
        setClarityAlert("Configuration error: API URL is not defined.");
        setIsClarityLoading(false);
        return;
      }
      try {
        // --- MODIFIED: Using environment variable for the API call ---
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}api/v1/generate_clarity_alert`, {
        // --- END MODIFICATION ---
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ reviews: MOCK_REVIEWS }),
        });

        if (!response.ok) {
            const errorData: { error?: string; detail?: string; message?: string } = await response.json().catch(() => ({ message: `Server error: ${response.status}` }));
            throw new Error(errorData.error || errorData.detail || errorData.message || `HTTP error! Status: ${response.status}`);
        }

        const data: { clarity_alert: string | null; error?: string } = await response.json();
        if (data.error) {
            console.error("Clarity Alert API Error:", data.error);
            setClarityAlert(`Error: ${data.error}`);
        } else {
            setClarityAlert(data.clarity_alert);
        }
      } catch (error: unknown) {
        let errorMessage = 'Network error occurred.';
        if (error instanceof Error) {
            errorMessage = error.message;
        }
        console.error("Error fetching clarity alert:", error);
        setClarityAlert(`Error fetching clarity alert: ${errorMessage}`);
      } finally {
        setIsClarityLoading(false);
      }
    };
    
    fetchClarityAlert(); 
  }, []);

  const analyzeReview = async (
    reviewText: string,
    setLoading: React.Dispatch<React.SetStateAction<boolean>>,
    setAnalysis: React.Dispatch<React.SetStateAction<AnalysisResult | null>>,
    isUserInput: boolean = false
  ) => {
    setLoading(true);
    if (isUserInput) setApiError(null);
    if (!process.env.NEXT_PUBLIC_API_URL) {
      const errorMsg = "Configuration error: API URL is not defined.";
      if (isUserInput) setApiError(errorMsg);
      else setAnalysis({ error: errorMsg, authenticity_score: 0, reasoning: "" });
      setLoading(false);
      return;
    }
    try {
      // --- MODIFIED: Using environment variable for the API call ---
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}api/v1/analyze_review_authenticity`, {
      // --- END MODIFICATION ---
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ review_text: reviewText }),
      });

      if (!response.ok) {
          const errorData: { error?: string; detail?: string; message?: string } = await response.json().catch(() => ({ message: `Server error: ${response.status}` }));
          throw new Error(errorData.error || errorData.detail || errorData.message || `HTTP error! Status: ${response.status}`);
      }

      const data: AnalysisResult = await response.json();

      if (data.error) {
          console.error("Authenticity API Error:", data.error);
          if (isUserInput) setApiError(data.error);
          else setAnalysis({ error: data.error, authenticity_score: 0, reasoning: "" });
      } else {
          setAnalysis(data);
      }
    } catch (error: unknown) {
      let errorMessage = 'Network error occurred.';
      if (error instanceof Error) {
          errorMessage = error.message;
      }
      console.error("Error analyzing review:", error);
      if (isUserInput) setApiError(`Failed to analyze review: ${errorMessage}`);
      else setAnalysis({ error: `Failed to analyze: ${errorMessage}`, authenticity_score: 0, reasoning: "" });
    } finally {
      setLoading(false);
    }
  };

  const handleUserInputClarity = async () => {
    if (!userInputReview.trim()) {
        setApiError('Please enter a review for clarity analysis.');
        return;
    }
    setIsUserInputClarityLoading(true);
    setApiError(null);
    setUserInputClarityAlert(null);
    setUserInputAuthenticityAnalysis(null);

    if (!process.env.NEXT_PUBLIC_API_URL) {
        setApiError("Configuration error: API URL is not defined.");
        setIsUserInputClarityLoading(false);
        return;
    }

    try {
      // --- MODIFIED: Using environment variable for the API call ---
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}api/v1/generate_clarity_alert`, {
      // --- END MODIFICATION ---
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ reviews: [userInputReview] }),
        });

        if (!response.ok) {
            const errorData: { error?: string; detail?: string; message?: string } = await response.json().catch(() => ({ message: `Server error: ${response.status}` }));
            throw new Error(errorData.error || errorData.detail || errorData.message || `HTTP error! Status: ${response.status}`);
        }

        const data: { clarity_alert: string | null; error?: string } = await response.json();

        if (data.error) {
            setApiError(data.error);
        } else {
            setUserInputClarityAlert(data.clarity_alert);
        }
    } catch (error: unknown) {
        let errorMessage = 'Network error occurred.';
        if (error instanceof Error) {
            errorMessage = error.message;
        }
        console.error('User input clarity alert failed:', error);
        setApiError(`Failed to get clarity alert: ${errorMessage}`);
    } finally {
        setIsUserInputClarityLoading(false);
    }
  };


  return (
    <main className="container mx-auto p-8 font-sans">
      <h1 className="text-3xl font-bold mb-2 text-center">AI-Powered Review Analysis</h1>
      <p className="mb-6 text-gray-600 text-center">Analyze review authenticity and generate clarity alerts.</p>

      {/* --- User Input Section --- */}
      <div className="mb-10 p-6 border border-gray-300 rounded-lg shadow-md bg-white">
        <h2 className="text-2xl font-bold mb-4 text-gray-800">Analyze Your Own Review</h2>
        <textarea
            className="w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 text-black text-base mb-4"
            rows={6}
            placeholder="Enter your product review text here..."
            value={userInputReview}
            onChange={(e) => {
                setUserInputReview(e.target.value);
                setApiError(null);
                setUserInputClarityAlert(null);
                setUserInputAuthenticityAnalysis(null);
            }}
        ></textarea>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button
                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg shadow-md transition-all duration-200 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed"
                onClick={() => analyzeReview(userInputReview, setIsUserInputAuthenticityLoading, setUserInputAuthenticityAnalysis, true)}
                disabled={isUserInputAuthenticityLoading || !userInputReview.trim()}
            >
                {isUserInputAuthenticityLoading ? 'Analyzing Authenticity...' : 'Analyze Authenticity'}
            </button>
            <button
                className="flex-1 bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-lg shadow-md transition-all duration-200 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed"
                onClick={handleUserInputClarity}
                disabled={isUserInputClarityLoading || !userInputReview.trim()}
            >
                {isUserInputClarityLoading ? 'Generating Clarity Alert...' : 'Generate Clarity Alert'}
            </button>
        </div>

        {apiError && (
            <p className="text-red-600 bg-red-100 p-3 rounded-md mt-4 text-center border border-red-300">
                Error: {apiError}
            </p>
        )}

        {/* User Input Authenticity Analysis Results */}
        {userInputAuthenticityAnalysis && (
            <div className="mt-8 p-6 border border-gray-300 rounded-lg shadow-lg bg-white text-gray-800">
                <h3 className="text-xl font-bold mb-4 text-blue-700">Your Review Authenticity Analysis:</h3>
                {userInputAuthenticityAnalysis.error ? (
                    <p className="text-red-600">Error: {userInputAuthenticityAnalysis.error}</p>
                ) : (
                    <>
                        <p className="text-lg font-medium mb-2">
                            Score: <span className="font-bold">{(userInputAuthenticityAnalysis.authenticity_score * 100).toFixed(0)}%</span>
                        </p>
                        <div className="authenticity-bar-container">
                            <div
                                className={`authenticity-bar ${
                                    userInputAuthenticityAnalysis.authenticity_score <= 0.2 ? 'red' :
                                    userInputAuthenticityAnalysis.authenticity_score <= 0.5 ? 'orange' :
                                    userInputAuthenticityAnalysis.authenticity_score <= 0.7 ? 'yellow-green' :
                                    userInputAuthenticityAnalysis.authenticity_score <= 0.9 ? 'green' :
                                    'dark-green'
                                }`}
                                style={{ width: `${(userInputAuthenticityAnalysis.authenticity_score * 100)}%` }}
                            ></div>
                        </div>
                        <p className="text-lg mt-4">
                            <strong>Reasoning:</strong> {userInputAuthenticityAnalysis.reasoning}
                        </p>
                    </>
                )}
            </div>
        )}

        {userInputClarityAlert && (
            <div className="mt-6 p-6 border border-gray-300 rounded-lg shadow-lg bg-white text-gray-800">
                <h3 className="text-xl font-bold mb-4 text-purple-700">Your Review Clarity Alert:</h3>
                <p className="text-lg">{userInputClarityAlert}</p>
            </div>
        )}
      </div>

      <h1 className="text-3xl font-bold mb-2 mt-10 text-center text-gray-800">Product Review Examples</h1>
      <p className="mb-6 text-gray-600 text-center">See how the AI analyzes pre-defined review scenarios.</p>

      <div className="mb-10 p-6 border border-gray-300 rounded-lg shadow-md bg-white">
        <h2 className="text-2xl font-bold mb-4 text-gray-800">Overall Product Review Clarity Analysis</h2>
        <ClarityAlert alertText={clarityAlert} isLoading={isClarityLoading} />
      </div>

      <hr className="my-8" />

      <h2 className="text-2xl font-bold mb-4 text-gray-800">Authenticity Analysis of Example Reviews</h2>

      <div className="mb-6 p-4 border border-gray-300 rounded-lg shadow-sm bg-white">
        <p className="italic mb-2 text-gray-700">{MOCK_SINGLE_REVIEW_GOOD}</p>
        <button
          onClick={() => analyzeReview(MOCK_SINGLE_REVIEW_GOOD, setIsGoodReviewLoading, setGoodReviewAnalysis, false)}
          className="bg-blue-500 hover:bg-blue-600 text-white text-sm px-4 py-2 rounded disabled:opacity-50 disabled:cursor-not-allowed"
          disabled={isGoodReviewLoading}
        >
          {isGoodReviewLoading ? 'Analyzing...' : 'Analyze Authenticity'}
        </button>
        <AuthenticityReport analysis={goodReviewAnalysis} isLoading={isGoodReviewLoading} />
      </div>

      <div className="mb-6 p-4 border border-gray-300 rounded-lg shadow-sm bg-white">
        <p className="italic mb-2 text-gray-700">{MOCK_SINGLE_REVIEW_FAKE}</p>
          <button
          onClick={() => analyzeReview(MOCK_SINGLE_REVIEW_FAKE, setIsFakeReviewLoading, setFakeReviewAnalysis, false)}
          className="bg-blue-500 hover:bg-blue-600 text-white text-sm px-4 py-2 rounded disabled:opacity-50 disabled:cursor-not-allowed"
          disabled={isFakeReviewLoading}
        >
          {isFakeReviewLoading ? 'Analyzing...' : 'Analyze Authenticity'}
        </button>
        <AuthenticityReport analysis={fakeReviewAnalysis} isLoading={isFakeReviewLoading} />
      </div>

    </main>
  );
}
