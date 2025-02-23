# Normal distribution and how to test it

## Normal Distribution
- **Definition**: A continuous probability distribution forming a symmetric bell-shaped curve.
- **Parameters**: Mean (µ), Standard Deviation (σ)
- **Use Case**: Normal distribution is assumed in most of the statistical tests and methods.

---

## Normality Tests

### 1. Visual Methods

While plotting is often reliable, it is a subjective approach and prone to errors.
- Histogram: Look for a bell-shaped curve.
- QQ Plot: Look for points lying along a straight line.
- KDE Plot: Look for a smooth, symmetric curve.
- Violin Plot: Look for a symmetric, bell-shaped violin.

#### Histogram
A histogram displays the distribution of your data by showing the frequency of data points within specified ranges (bins).
- **How to Use**: Plot your data and look for a bell-shaped curve.
- **Interpretation**: A normal distribution will appear as a symmetric, bell-shaped curve centered around the mean.

#### QQ Plot (Quantile-Quantile Plot)
A QQ plot compares the quantiles of your data against the quantiles of a normal distribution.
- **How to Use**: Plot your data’s quantiles against the quantiles of a normal distribution.
- **Interpretation**: If the data is normally distributed, the points will lie approximately along a straight line.

#### KDE Plot (Kernel Density Estimate)
A KDE plot is a smoothed version of the histogram, providing an estimate of the probability density function of the data.
- **How to Use**: Plot the KDE of your data.
- **Interpretation**: A normal distribution will appear as a smooth, symmetric curve centered around the mean.

#### Violin Plot
A violin plot combines aspects of a box plot and a KDE plot, showing the distribution of the data across different levels.
- **How to Use**: Plot the violin plot of your data.
- **Interpretation**: A normal distribution will appear as a symmetric, bell-shaped violin.

### 2. Statistical Methods
#### Shapiro-Wilk Test
- **Parameters:**
    1. **Statistic (W):**
        - **Range**: (0 ≤ W ≤ 1)
        - **Interpretation:** Measures how well the data conforms to a normal distribution. A value close to 1 indicates the data is normally distributed.
    2. **p-value:** A low p-value (<0.05) suggests data is not normal.
        - **Range**: (0 ≤ p-value ≤ 1)
        - **Interpretation:** A low p-value, typically (< 0.05), suggests that the data is not normally distributed.
    3. **Sample size**: 3 to 2000
- **Advantages:**
    - **Powerful:** More powerful than other tests for detecting deviations from normality.
    - **Widely Used:** Commonly used in many statistical software packages.
- **Limitations:**
    - **Sample Size:** Less effective for very large sample sizes.
    - **Sensitivity:** Sensitive to small deviations from normality.


#### Kolmogorov-Smirnov Test
- **Parameters:**
    1. **Statistic (D):**
        - **Range**: (0 ≤ D ≤ 1)
        - **Interpretation:** Represents the maximum difference between the empirical distribution function (EDF) and the cumulative distribution function (CDF). A smaller (D) value indicates a closer fit to the reference distribution.
    2. **p-value:**
        - **Range**: (0 ≤ p-value ≤ 1)
        - **Interpretation:** A low p-value, typically (< 0.05), suggests that the data is not normally distributed.
    3. **Sample size**: 3 or more
- **Advantages:**
    - **Non-parametric:** No assumption about the distribution of data.
    - **Versatile:** Can be used for both one-sample and two-sample tests.
        - One-sample test compares to normal distribution
        - Two-samples test compares whether two datasets follow the same distribution

- **Limitations:**
    - **Sample Size:** Requires a reasonably large sample size for accurate results.


#### Anderson-Darling Test
- **Parameters:**
    1. **Statistic (A²):**
        - **Range**: (0 ≤ A²)
        - **Interpretation:** Measures the distance between the EDF and the CDF, with more weight given to the tails. A larger (A²) value indicates a greater deviation from the reference distribution.
    2. **Critical Values:**
        - **Range**: Varies based on sample size and significance level.
        - **Interpretation:** Used to determine if the test statistic (A²) is significant. An (A²) value exceeding the critical value suggests that the data is not normally distributed.
    3. **Sample size**: 20 or more
- **Advantages:**
    - **Tail Sensitivity:** More sensitive to deviations in the tails of the distribution.
    - **Powerful:** Generally more powerful than the K-S test for detecting deviations from normality.
- **Limitations:**
    - **Sample Size:** Requires a reasonably large sample size for accurate results.
    - **Sensitivity:** More complex to calculate and interpret than the K–S test.


#### Lilliefors Test
- **Parameters:**
    1. **Statistic (D):**
        - **Range**: (0 ≤ D ≤ 1)
        - **Interpretation:** Similar to the K-S test, it measures the maximum difference between the EDF and the CDF but adjusted for estimated parameters. A smaller (D) value indicates a closer fit to the reference distribution.
    2. **p-value:**
        - **Range**: (0 ≤ p-value ≤ 1)
        - **Interpretation:** A low p-value, typically (< 0.05), suggests that the data is not normally distributed.
    3. **Sample size**: 3 or more
- **Advantages:**
    - **Parameter Estimation:** Can be used when the population mean and standard deviation are unknown.
    - **Improved K-S Test:** Corrects for small values at the tails of probability distributions.
- **Limitations:**
    - **Sample Size:** Requires a reasonably large sample size for accurate results.
    - **Power:** Generally has lower power compared to the Anderson-Darling and Shapiro-Wilk tests


### 3. Distance Measures

Distance measures are another reliable and more intuitive way to test normality.

#### Bhattacharyya Distance
- **Statistic (D):**
    - **Range**: (0 ≤ D)
    - **Interpretation:** Measures the shape similarity (overlap) between two probability distributions. A value of 0 indicates identical distributions, while larger values indicate greater dissimilarity.
- **Advantages:**
    - **Simplicity:** Easy to compute and interpret.
    - **Overlap Measurement:** Provides a direct measure of the overlap between two distributions.
- **Limitations:**
    - **Not a Metric:** Does not satisfy the triangle inequality.
    - **Sensitivity:** Can be sensitive to small changes in the distributions.

#### Hellinger Distance
- **Statistic (H):**
    - **Range**: (0 ≤ H ≤ 1)
    - **Interpretation:** Measures the shape similarity (overlap) between two probability distributions. A value of 0 indicates identical distributions, while a value of 1 indicates completely dissimilar distributions.
- **Advantages:**
    - **Bounded Metric:** Always ranges between 0 and 1, making it easy to interpret.
    - **Symmetry:** Symmetric and satisfies the triangle inequality.
- **Limitations:**
    - **Computational Complexity:** Can be computationally intensive for large datasets.
    - **Sensitivity:** May be sensitive to small changes in the distributions.

#### Kullback-Leibler (KL) Divergence
- **Statistic (D_KL):**
    - **Range**: (0 ≤ D_KL)
    - **Interpretation:** Measures the divergence between two probability distributions. A value of 0 indicates identical distributions, while larger values indicate greater divergence. Not exactly a distance but can be used this way.
- **Advantages:**
    - **Information Gain:** Provides a measure of the information gain when using one distribution to approximate another.
    - **Asymmetry:** Useful for applications where the direction of divergence matters.
- **Limitations:**
    - **Not Symmetric:** (D_KL(P||Q) ≠ DKL(Q||P)).
    - **Infinite Values:** Can yield infinite values if the distributions have non-overlapping support.