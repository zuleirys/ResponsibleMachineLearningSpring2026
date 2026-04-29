# Individual Homework 05 Report
## Applied Adversarial Audit on COMPAS

### Overview

This report summarizes the main findings from the Lecture 05 applied assignment on adversarial machine learning using the ProPublica COMPAS dataset. The notebook extends the earlier COMPAS workflow into three security-focused attack paths: PGD evasion, targeted label poisoning, and membership inference. The goal is not only to measure whether performance changes under attack, but also to understand whether fairness or privacy can fail even when average model quality still looks acceptable.

### 1. PGD Evasion Audit

The PGD audit was run on both the logistic regression and gradient-boosted tree models across `epsilon = 0.25, 0.5, 1.0, 2.0`. The fairness lens used here was race-specific false positive rates together with AIR, where the favorable outcome is a predicted low-risk classification and AIR is measured as the African-American low-risk rate divided by the Caucasian low-risk rate.

The two models were not equally vulnerable. In the clean baseline, AIR was already below the `0.80` threshold for both models: `0.768` for logistic regression and `0.776` for the gradient-boosted tree. That means there was no new threshold crossing within the positive attack budgets because the fairness concern already existed before the attack. Under stronger perturbations, however, the models diverged in different directions. By `epsilon = 2.0`, the logistic regression AIR rose to about `1.276`, while the gradient-boosted tree AIR rose only to about `0.851`. This implies that the same PGD-style perturbation can shift group-level fairness in materially different ways depending on model class.

The high-stakes implication is that model selection should not rely only on clean test AUC. A model can look acceptable under ordinary evaluation and still react to adversarial perturbations in a way that changes race-specific outcomes. In practice, this means a deployment decision should include adversarial fairness stress testing rather than only clean performance benchmarks.

### 2. Poisoning Loop With Fairness Monitoring

The poisoning experiment flipped a fraction of non-recidivist training labels from `0` to `1` within a targeted race and then retrained the gradient-boosted tree. I evaluated both the original African-American-targeted version and the Caucasian-targeted extension requested in the lecture.

This was the strongest fairness finding in the notebook. For African-American targeting, AIR fell from the clean baseline of `0.776` to `0.559` at a `10%` poison rate and to `0.155` at `15%`, while test AUC still remained around `0.980`. For Caucasian targeting, AIR moved in the opposite direction and reached `1.473` at a `10%` poison rate while AUC was still approximately `0.980`. In other words, the attack could push AIR outside the `[0.80, 1.25]` band without causing a large visible drop in average predictive performance.

This is exactly the “stealth zone” problem emphasized in lecture. The notebook found `10` attack settings where fairness degraded outside the acceptable band while AUC declined by no more than `2` percentage points. That makes poisoning particularly concerning from a governance perspective because a team monitoring only headline accuracy might conclude that the model is still functioning normally while subgroup harm is worsening sharply.

The PSI check makes that point even stronger. For every poison rate and both target-race variants, the maximum numeric-feature PSI remained `0.0`. A feature-only drift monitor would therefore miss the attack entirely. The labels were corrupted, but the feature distributions never changed, so PSI gave a false sense of safety.

### 3. Membership Inference Depth

The shadow-model membership inference pipeline produced an MI AUC of `0.514` for logistic regression and `0.512` for the gradient-boosted tree. These values are not catastrophic, but they are still above the random baseline of `0.50`, which means membership status is detectable to some degree from model outputs alone.

The lecture question about whether the generalization gap predicts MI AUC produced a mixed answer in this notebook. The gradient-boosted tree had the larger AUC generalization gap (`0.0171` versus `0.0049` for logistic regression), but the logistic regression had the slightly larger MI AUC (`0.514` versus `0.512`). With only two baseline models, this is not a statistically meaningful test, but directionally it suggests that generalization gap alone is not enough to predict privacy leakage in this setting.

The L2 regularization sweep for logistic regression gave the clearest mitigation result in the assignment. Tightening regularization to `C = 0.01` reduced MI AUC from `0.514` to `0.506`. At the same time, clean test AUC improved slightly from `0.985` to `0.988`, and the African-American versus Caucasian AIR stayed at `0.768`. That means stronger regularization improved privacy exposure without introducing an obvious clean-performance or fairness penalty in this experiment.

### 4. Highest-Risk Finding And Mitigations

Across all three parts, the single highest-risk finding was the membership-inference exposure of the logistic regression model. I treat this as the top risk because it directly exposes individual-record privacy through the normal prediction interface and does not require poisoning the training pipeline or engineering deployment-time feature changes.

The proactive mitigation supported by the experiments is to deploy the more strongly regularized logistic regression with `C = 0.01` when privacy risk is a priority. This lowers MI AUC from `0.514` to `0.506` while preserving strong clean performance (`0.988` test AUC) and leaving the race AIR essentially unchanged.

The reactive mitigation supported by the experiments is to clip or coarsen released probabilities before exposing them through an API. In the notebook, clipping probabilities for the highest-risk baseline model reduced MI AUC from `0.514` to `0.502`, with clean test AUC at `0.978` and African-American AIR still `0.768`. This does not eliminate all privacy risk, but it materially reduces the attacker’s confidence-gap signal while leaving the class decision boundary largely intact.

### Conclusion

The main lesson from Lecture 05 is that average predictive quality does not tell the full governance story. Under adversarial pressure, a model can remain high-performing on aggregate metrics while still becoming unfair under poisoning, unstable under PGD perturbation, or privacy-leaky under membership inference. Security, fairness, and robustness are therefore not separate evaluation tracks. They are connected failure modes that need to be audited together.
