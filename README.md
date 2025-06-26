# ecommerce-analytics-pipeline

A scalable data analytics pipeline for processing e-commerce transactions using **PySpark**, **Pandas**, **Apache Arrow**, and **DuckDB**. This project demonstrates how to analyze customer purchase behavior, extract meaningful insights, and segment users based on transaction patterns.

---

## 🚀 Overview

This pipeline processes raw e-commerce transaction data and performs:

- Data ingestion using **PySpark**
- Efficient in-memory data transfer via **Apache Arrow**
- Feature engineering with **Pandas**
- Fast SQL-based segmentation using **DuckDB**

---

## 📊 Sample Use Case

**Customer Purchase Behavior Analysis**:
- Identify high-value, engaged, and inactive users
- Calculate metrics like purchase frequency, recency, and category preferences
- Output daily user segments for recommendations or marketing

---

## 🧰 Tech Stack

| Tool        | Role                                       |
|-------------|--------------------------------------------|
| PySpark     | Distributed data processing                |
| Apache Arrow| Fast in-memory data exchange               |
| Pandas      | Lightweight feature transformations        |
| DuckDB      | Fast analytical SQL queries on in-memory data |

---

## 📁 Project Structure

```text
ecommerce-analytics-pipeline/
├── data/                    # Raw or cleaned datasets
├── notebooks/               # Jupyter notebooks for development
├── scripts/                 # PySpark & DuckDB processing scripts
├── output/                  # Final processed results
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecommerce-analytics-pipeline.git
   cd ecommerce-analytics-pipeline
   ```

2. **Create a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. ***Download the dataset**
    - Source: [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
    - Save as: data/online_retail.xlsx


##  How to Run
Run the full pipeline from Jupyter notebook or execute scripts in scripts/:
    ```bash
    python scripts/process_transactions.py
    ```
