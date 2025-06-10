# 🐦 Twitter Sentiment Analyzer using Tweepy & TextBlob

A simple yet powerful Python project that fetches live tweets using Twitter API (via Tweepy), processes and analyzes them using natural language processing (NLP) via TextBlob, and presents the sentiment results clearly. This project demonstrates skills in API integration, data cleaning, sentiment analysis, and basic data reporting — all in under 100 lines of clean code.

## 🚀 Project Overview

This tool:
- Uses the **Twitter v2 API** with **Tweepy** to fetch real-time tweets based on a keyword.
- Cleans raw tweet text using **Regex**.
- Analyzes sentiment (Positive / Neutral / Negative) with **TextBlob**, a simple NLP library.
- Calculates and displays sentiment percentages.
- Lists top positive and negative tweets found for quick insight.

## ✅ Features

- 🔍 Live tweet fetching using `search_recent_tweets()`
- 🧹 Custom tweet cleaner to remove mentions, links, and special characters
- 🤖 Sentiment analysis using `TextBlob` polarity score
- 📊 Results summarization with sentiment percentages
- 📄 Minimal, easy-to-read Python code

  💡 Future Improvements
- Visualize sentiment trends using matplotlib or Plotly

- Save results to a CSV or database

- Deploy as a Flask web app for UI-based interaction

- Use advanced NLP models like VADER or transformer-based sentiment models

## 📦 Dependencies

Install required libraries with:

```bash
pip install tweepy textblob
