# Rubus LSTM

# ![0xRubusLtsm](./public/agents/0xRubusLtsm.png)

# LSTM model API

This is a FastAPI-based API for stock price prediction using an LSTM model, integrated with Alpha Vantage for data acquisition and PostgreSQL for persistence. It supports data preparation, model training, evaluation, prediction, and visualization.

## Features
- **Data Acquisition**: Fetch data from multiple Alpha Vantage APIs (timeseries, cryptocurrencies, foreignexchange, and more).
- **Data Preparation**: Normalize data and generate train/validation datasets.
- **Model Management**: Define, train, and evaluate LSTM models.
- **Prediction**: Forecast the next day's stock price.
- **Visualization**: Generate plots (e.g., actual vs. predicted, train vs. val).
- **Configuration**: Manage API keys and plot settings.

## Prerequisites
- Python 3.9+
- Docker (optional, for containerized deployment)
- PostgreSQL (if running locally without Docker)
- Alpha Vantage API key (get one at [alphavantage.co](https://www.alphavantage.co/support/#api-key))

## Setup

### Local Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd rubus-ltsm
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables in a .env file:
   ```bash
   echo "DATABASE_URL=postgresql://user:password@localhost:5432/stock_db" >> .env
   echo "ALPHA_VANTAGE_KEY=your_api_key_here" >> .env
   ```
4. Run the app:  
    ```bash
    uvicorn app.main:app --reload
   ```

### Docker Installation
1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```
2. Ensure .env is set as above and placed in the project root.

## Usage
- Access the API at http://localhost:8000.
- Explore endpoints via Swagger UI at http://localhost:8000/docs.

### Example Workflow
1. Set Configuration:
   ```bash
   curl -X POST "http://localhost:8000/config/set" -H "Content-Type: application/json" -d '{"alpha_vantage_key": "your_api_key", "xticks_interval": 30}'
   ```
2. Acquire Data:
   ```bash
   curl -X POST "http://localhost:8000/data/acquire" -H "Content-Type: application/json" -d '{"symbol": "IBM"}'
   ```
3. Define and Train a Model:
   - Define: POST /model/define with {"stock_symbol": "IBM"}.
   - Train: POST /model/train with {"model_id": 1, "dataset_id": 1}.

4. Evaluate and Predict:
   - Evaluate: POST /model/evaluate with {"training_run_id": 1}.
   - Predict: POST /model/predict with {"training_run_id": 1}.
   
5. Generate Plots:
   ```bash
   curl -X POST "http://localhost:8000/plot/prices" -H "Content-Type: application/json" -d '{"training_run_id": 1, "plot_type": "actual_vs_predicted"}'
   ```

## API Endpoints

See detailed endpoint documentation in the Swagger UI or the openapi.json file at /openapi.json.

## Project Structure
   ```bash
   rubus-ltsm/
    ├── app/              # FastAPI application
    │   ├── config/       # Configuration settings
    │   ├── main.py       # App entry point
    │   ├── models/       # SQLModel database models
    │   ├── routes/       # API endpoints
    │   ├── services/     # Business logic
    │   └── utils/        # Helper classes
    ├── docker-compose.yml
    ├── Dockerfile
    └── requirements.txt
   ```



## 📜 License
MIT License - Free to use and contribute!

## 📝 **Author**
- 👤 0xRubusData 
- 📧 Contact: 0xRubusData@gmail.com
- 🌍 GitHub: https://github.com/0xrubusdata/rubus-ltsm

## 🌐 Connect with Us
- **Twitter (X)**: [0xRubusData](https://x.com/Data0x88850)
- **Website**: [RubusLab](https://rubus-lab.vercel.app/)

## 🤝 Contributing
Contributions are welcome! Open an issue or submit a PR.

---
🚀 **Stay tuned for updates as Rubus-Ltsm evolves!**
