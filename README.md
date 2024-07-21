# world-stats-using-streamlit-plotly
This Streamlit application provides an interactive dashboard to visualize and analyze various metrics for countries around the world. It includes a world map with bubble sizes representing different metrics, top-level insights, bar charts, histograms, box plots, and a correlation heatmap.
![Screenshot 2024-07-18 165030](https://github.com/user-attachments/assets/65407409-eb06-4a49-b630-fedf85d3f65b)
## Features

- **Interactive World Map**: Visualize countries on a map with bubble sizes representing a selected metric.
- **Top-level Metrics**: Display key metrics such as the total number of countries, average economic score, total population, and average growth rate.
- **Top 5 Countries by Population**: A bar chart showing the top 5 countries based on population.
- **Histograms**: View the distribution of the selected metric across different continents.
- **Box Plots**: Compare key metrics across continents.
- **Correlation Heatmap**: Analyze the correlation between different metrics.
- **Dynamic Insights**: Highlight the top and bottom countries for the selected metric.

## Dataset
3 dataset6s are provided and all three are necessary as we have manipulated datasets in the main code
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bharat7676/app.git
   cd app.py
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your dataset**:
   - Place your datasets file in the project directory and update the file path in the script.

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run enhanced_dashboard_app.py
   ```

2. **Open your browser**:
   - The app will automatically open in your default web browser. If not, navigate to `http://localhost:8501`.

## Project Structure

```
enhanced-dashboard-app/
├── app.py
├── requirements.txt
└── path_to_your_dataset.csv
```

- `app.py`: The main Streamlit app script.
- `requirements.txt`: List of required Python packages.
- `path_to_your_dataset.csv`: Your dataset file (replace with the actual filename).

## Requirements

- Python 3.7 or higher
- Streamlit
- Pandas
- Plotly

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
- [Pandas](https://pandas.pydata.org/)

## Contact

For any questions or suggestions, feel free to contact [Bharatkumar](mailto:bharatkumarsalalli2.0@gmail.com).
