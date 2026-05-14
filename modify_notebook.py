import json

notebook_path = r"d:\THE CODE\Deep_Learning\2_1_MARKDOWN_perceptron_regression_issue.ipynb"

markdown_content = r"""## Using a Library (Scikit-Learn)

You might be wondering: *"Why do we have to build this manually? Isn't there a library for this?"*

The term **Perceptron** is historically reserved strictly for **classification** (specifically using a step function). When you remove the step function and use a linear activation to predict continuous values, you are essentially just doing **Linear Regression trained with Gradient Descent**.

Because of this terminology, libraries like `scikit-learn` do not have a `RegressionPerceptron`. Instead, you would use:
- `sklearn.linear_model.LinearRegression` (Uses the Ordinary Least Squares exact mathematical solution)
- `sklearn.linear_model.SGDRegressor` (Uses Gradient Descent to find the weights, which is **exactly what the manual code above does**)

Here is how you do the exact same thing using `scikit-learn`'s `SGDRegressor`:

```python
import numpy as np
from sklearn.linear_model import SGDRegressor

# 1. Generate the same linear dummy data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
y = y.flatten()

# 2. Train the model using Stochastic Gradient Descent (SGD)
# This is the library equivalent of our manual "Regression Perceptron"
# Using squared_error loss makes it identical to our manual math
model = SGDRegressor(loss='squared_error', learning_rate='constant', eta0=0.01, max_iter=1000)
model.fit(X, y)

# 3. View the learned weights and bias
print(f"Learned Weight: {model.coef_[0]:.4f} (True: 3)")
print(f"Learned Bias: {model.intercept_[0]:.4f} (True: 4)")

# 4. Make a prediction
X_test = np.array([[1.5]])
print(f"Prediction for X=1.5: {model.predict(X_test)[0]:.4f}")
```
"""

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
except Exception as e:
    pass

new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": markdown_content.splitlines(True)
}

nb['cells'].append(new_cell)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
