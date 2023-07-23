# SyncMate - Autonomous Social Network AI Co-pilot

SyncMate is an autonomous AI agent developed during the AGI House hackathon on autonomous AI agents. It aims to maximize every interaction's potential and elevate communication by providing context, summaries, and expert insights for your social network activities. This README provides an overview of this one-day project, installation instructions, and examples of queries along with the corresponding responses.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

SyncMate is an AI agent designed to connect to various social media and communications channels, currently supporting Slack and Bard queries. It actively tracks updates from your network and provides you with insightful summaries, and can even answer your questions about your network and the people within it. With SyncMate, you have an autonomous co-pilot to assist you in making the most out of your social interactions.

## Features

- **Contextual Insights**: SyncMate offers contextual information about your social network interactions, helping you understand the broader picture and implications of your communications.

- **Summaries**: Stay updated with brief and concise summaries of your network's activities, saving you valuable time while ensuring you remain well-informed.

- **Expert Answers**: Ask questions about your network or individuals, and SyncMate will provide expert-level insights based on the available data.

- **Multi-platform Support**: Currently, SyncMate supports Slack and Bard queries, and more integrations may be added in the future.

## Installation

To get started with SyncMate, follow these installation steps:

1. Clone the repository.

2. Install the required dependencies:
   ```
   pip install openai bardapi langchain
   ```

3. Set up your API keys and credentials for the social media platforms you wish to integrate with SyncMate.

## Usage

To run SyncMate, see `agent.ipynb` for example integrations.

The agent will start monitoring your selected social media platforms and respond to your queries.

## Examples

Here are some example queries you can ask SyncMate along with the expected responses:

1. **Query**: "Give me a summary of today's Slack activity."
   - **Response**: "Today, there were 10 new messages and 5 files shared in Slack. The most discussed topics were project updates and planning for the upcoming event."

2. **Query**: "What are people saying about the new product launch?"
   - **Response**: "Opinions on the new product launch are mixed. Some users are excited about the features, while others are requesting more information about pricing and availability."

3. **Query**: "Tell me about John Doe."
   - **Response**: "John Doe is a seasoned software engineer with expertise in machine learning and data science. He has been with the company for three years and has contributed significantly to various projects."

4. **Query**: "Which team member has the most interactions this month?"
   - **Response**: "Jane Smith has the most interactions this month, with 72 interactions across different channels."

5. **Query**: "What topics are trending in the Bard community?"
   - **Response**: "The trending topics in the Bard community are AI ethics, quantum computing, and natural language processing."

Please note that these are simulated responses for illustrative purposes. The actual responses will be based on the data available from your connected social media platforms.

## Contributing

SyncMate was born in the AGI House autonomous agents one-day hackathon as a proof of concept. We welcome contributions to SyncMate! If you have any bug fixes, new features, or improvements, please submit a pull request. For major changes, please open an issue to discuss the proposed changes beforehand.

Thank you for your interest in SyncMate! If you encounter any issues or have further questions, please feel free to open an issue on the repository. We hope SyncMate enhances your social networking experience with its autonomous insights and assistance!
