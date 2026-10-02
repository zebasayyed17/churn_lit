# CHURN//LAB — Streamlit Package

This package hosts the finished Customer Churn Prediction HTML inside Streamlit.

## Files

- `streamlit_app.py` — Streamlit entrypoint.
- `customer_churn_prediction.html` — complete visual UI and browser-side prediction logic.
- `churn_model.pkl` — original trained model, kept with the package as the source model asset.
- `churnn.py` — original Streamlit/Python implementation, kept for reference.
- `requirements.txt` — Streamlit dependency.
- `.streamlit/config.toml` — matching Xscel-style cream/orange Streamlit shell.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

The HTML contains the model coefficients used for the browser-side prediction, so the Streamlit host does not need to execute the pickle during inference.
