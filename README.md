# Greener Future ✊ - Mini Data Challenge #3

Brought to you by the Data Community UNILAG

## Challenge Overview

Analyze the 3 global temperature datasets to gain insights into climate change trends over the last few centuries.

### Tasks

<details>
<summary><strong>Part 1: Analysis</strong></summary>

- Find a suitable way to fill in missing dates (if any)

From your analysis, answer the following questions:

- How has land and ocean average temperatures changed over time?
- Which warmed faster over time—land or ocean? By how much?
- How does land temperature vary with season?
- Which countries have experienced the fastest warming trends? Visualize this.

Notice how these questions deal with how "fast" the temperature is rising?

</details>

<details>
<summary><strong>Part 2: ML Model</strong></summary>

The data provided ends in 2010-08-01.

- Drop the `LandAndOceanAverageTemperature` since it correlates with the target

- Build a machine learning model to predict `LandAverageTemperature` for the next `n` months based on the available features. (neural networks are not allowed)

- At the end of your submission, write a function named `predict_temperatures` that takes in an integer `n` and returns global temperatures for the next `n` months after 2010-08-01. (Jupyter notebooks are also accepted).

See the sample `submission.py` for more details.

</details>

## Submission Guidelines

### Timeline

- **Challenge Release:** Thursday 23rd, January 2025.
- **Submission Deadline:** February 8th, 2025 (11:59 PM)
- **Winner Announcement:** Someday between 10th and 15th of February depending on the number of submissions.

### Evaluation Criteria

Your submission will be evaluated based on:

- **Accuracy:** Evaluation of your model's predictions (40%).
- **Analysis:** Depth of analysis and insights (40%).
- **Clarity:** Clear presentation of findings and visualizations (20%).

For accuracy, aim for less than the baseline which is a root mean squared error (RMSE) of around 6.8. This is gotten from a model that predicts 15.0 for every month.

### Get Started

<details>
<summary>Click to expand</summary>

1. **Fork this repository.**
2. **Clone the repository** to your local machine.
3. _(optional)_ Create a virtual environment and install the required packages using `pip install -r requirements.txt`.
4. Complete the challenge and include:
   - Your code (only Python will be accepted, that is, either `submission.ipynb` or `submission.py`).
   - A summary of your findings (`summary.md`).
   - (Optional) Any visualizations (e.g., `.png`, `.pdf`) in the `visualizations` folder.
   - (Optional) `requirements.txt`
5. **Submit your work** by creating a branch named `submission-[your-name]` and opening a pull request.

</details>

## Dataset Details

<details>
<summary>Click to expand</summary>

Find all relevant datasets in the `/data` folder

- **Names:** GlobalTemperatures.csv, GlobalTemperaturesByCountry.csv, GlobalTemperaturesByState.csv
- **Source:** [Kaggle](https://www.kaggle.com/datasets/sachinsarkar/climate-change-global-temperature-data)
- **Warning:** Do not train your model using the source data directly. Use the provided train and test datasets to ensure fair evaluation.
  </details>

## Prizes and Recognition

- 🌟 The top submission will be featured on our [Twitter page](https://twitter.com/DataComUnilag) and the community Whatsapp group.
- 🏆 Leaderboard points will be awarded to all participants based on performance.

## Questions or Feedback?

For any inquiries, open an issue on this repo (not on your fork) or reach out to us on the community Whatsapp group.

Happy analyzing! 🚀
