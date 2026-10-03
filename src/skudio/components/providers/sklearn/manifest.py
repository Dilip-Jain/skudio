"""Manifest of scikit-learn components.

Each entry lists a small "basic" param set that the UI shows by default.
Advanced params fall back to introspection later; for now, users who need
a param not listed here type it as an "advanced" free-form entry.
"""

from __future__ import annotations

from skudio.components.metadata import ComponentMetadata, ParamDescriptor

_DOC_ROOT = "https://scikit-learn.org/stable/modules/generated/"


def _est(qn: str, display: str, params: list[ParamDescriptor], desc: str = "") -> ComponentMetadata:
    return ComponentMetadata(
        qualname=qn,
        display_name=display,
        category="estimator",
        task="classification",
        description=desc,
        doc_url=f"{_DOC_ROOT}{qn}.html",
        params=params,
    )


def _reg(qn: str, display: str, params: list[ParamDescriptor], desc: str = "") -> ComponentMetadata:
    return ComponentMetadata(
        qualname=qn,
        display_name=display,
        category="estimator",
        task="regression",
        description=desc,
        doc_url=f"{_DOC_ROOT}{qn}.html",
        params=params,
    )


def _pre(qn: str, display: str, params: list[ParamDescriptor], desc: str = "") -> ComponentMetadata:
    return ComponentMetadata(
        qualname=qn,
        display_name=display,
        category="preprocessing",
        description=desc,
        doc_url=f"{_DOC_ROOT}{qn}.html",
        params=params,
    )


def _p(name: str, default: object = None, **kwargs: object) -> ParamDescriptor:
    return ParamDescriptor(name=name, default=default, **kwargs)  # type: ignore[arg-type]


ESTIMATORS: list[ComponentMetadata] = [
    _est(
        "sklearn.linear_model.LogisticRegression",
        "Logistic Regression",
        [
            _p(
                "C",
                1.0,
                widget="number",
                min=0.0001,
                description="Inverse regularization strength.",
            ),
            _p("penalty", "l2", widget="select", choices=["l1", "l2", "elasticnet", None]),
            _p(
                "solver",
                "lbfgs",
                widget="select",
                choices=["lbfgs", "liblinear", "saga", "newton-cg"],
            ),
            _p("max_iter", 100, widget="int", min=1, tier="advanced"),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
        "Linear classifier for binary and multi-class problems.",
    ),
    _est(
        "sklearn.linear_model.RidgeClassifier",
        "Ridge Classifier",
        [
            _p("alpha", 1.0, widget="number", min=0.0),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _est(
        "sklearn.linear_model.SGDClassifier",
        "SGD Classifier",
        [
            _p("loss", "hinge", widget="select", choices=["hinge", "log_loss", "modified_huber"]),
            _p("alpha", 0.0001, widget="number", min=0.0),
            _p("max_iter", 1000, widget="int", tier="advanced"),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),


    _est(
        "sklearn.neighbors.KNeighborsClassifier",
        "K-Nearest Neighbors",
        [
            _p("n_neighbors", 5, widget="int", min=1),
            _p("weights", "uniform", widget="select", choices=["uniform", "distance"]),
        ],
    ),
    _est(
        "sklearn.tree.DecisionTreeClassifier",
        "Decision Tree",
        [
            _p("criterion", "gini", widget="select", choices=["gini", "entropy", "log_loss"]),
            _p("max_depth", None, widget="int", min=1),
            _p("min_samples_split", 2, widget="int", min=2, tier="advanced"),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _est(
        "sklearn.ensemble.RandomForestClassifier",
        "Random Forest",
        [
            _p("n_estimators", 100, widget="int", min=1),
            _p("criterion", "gini", widget="select", choices=["gini", "entropy", "log_loss"]),
            _p("max_depth", None, widget="int", min=1),
            _p("random_state", None, widget="int", tier="advanced"),
            _p("n_jobs", None, widget="int", tier="advanced"),
        ],
    ),
    _est(
        "sklearn.ensemble.GradientBoostingClassifier",
        "Gradient Boosting",
        [
            _p("n_estimators", 100, widget="int", min=1),
            _p("learning_rate", 0.1, widget="number", min=0.0),
            _p("max_depth", 3, widget="int", min=1),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _est(
        "sklearn.svm.SVC",
        "Support Vector Classifier",
        [
            _p("C", 1.0, widget="number", min=0.0001),
            _p("kernel", "rbf", widget="select", choices=["linear", "poly", "rbf", "sigmoid"]),
            _p("gamma", "scale", widget="select", choices=["scale", "auto"]),
            _p("probability", False, widget="toggle", tier="advanced"),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _est(
        "sklearn.naive_bayes.GaussianNB",
        "Gaussian Naive Bayes",
        [
            _p("var_smoothing", 1e-9, widget="number", tier="advanced"),
        ],
    ),
    _est(
        "sklearn.neural_network.MLPClassifier",
        "Multi-layer Perceptron",
        [
            _p("hidden_layer_sizes", [100], widget="text"),
            _p(
                "activation",
                "relu",
                widget="select",
                choices=["identity", "logistic", "tanh", "relu"],
            ),
            _p("max_iter", 200, widget="int", tier="advanced"),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
]


REGRESSORS: list[ComponentMetadata] = [
    _reg(
        "sklearn.linear_model.LinearRegression",
        "Linear Regression",
        [_p("fit_intercept", True, widget="toggle", tier="advanced")],
    ),
    _reg(
        "sklearn.linear_model.Ridge",
        "Ridge Regression",
        [
            _p("alpha", 1.0, widget="number", min=0.0),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _reg(
        "sklearn.linear_model.Lasso",
        "Lasso",
        [
            _p("alpha", 1.0, widget="number", min=0.0),
            _p("max_iter", 1000, widget="int", tier="advanced"),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _reg(
        "sklearn.tree.DecisionTreeRegressor",
        "Decision Tree Regressor",
        [
            _p("max_depth", None, widget="int", min=1),
            _p("min_samples_split", 2, widget="int", min=2, tier="advanced"),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _reg(
        "sklearn.ensemble.RandomForestRegressor",
        "Random Forest Regressor",
        [
            _p("n_estimators", 100, widget="int", min=1),
            _p("max_depth", None, widget="int", min=1),
            _p("random_state", None, widget="int", tier="advanced"),
            _p("n_jobs", None, widget="int", tier="advanced"),
        ],
    ),
    _reg(
        "sklearn.ensemble.GradientBoostingRegressor",
        "Gradient Boosting Regressor",
        [
            _p("n_estimators", 100, widget="int", min=1),
            _p("learning_rate", 0.1, widget="number", min=0.0),
            _p("max_depth", 3, widget="int", min=1),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _reg(
        "sklearn.svm.SVR",
        "Support Vector Regressor",
        [
            _p("C", 1.0, widget="number", min=0.0001),
            _p("kernel", "rbf", widget="select", choices=["linear", "poly", "rbf", "sigmoid"]),
            _p("gamma", "scale", widget="select", choices=["scale", "auto"]),
        ],
    ),
    _reg(
        "sklearn.neighbors.KNeighborsRegressor",
        "K-Nearest Neighbors Regressor",
        [
            _p("n_neighbors", 5, widget="int", min=1),
            _p("weights", "uniform", widget="select", choices=["uniform", "distance"]),
        ],
    ),
]

TRANSFORMERS: list[ComponentMetadata] = [
    _pre(
        "sklearn.impute.SimpleImputer",
        "Simple Imputer",
        [
            _p(
                "strategy",
                "mean",
                widget="select",
                choices=["mean", "median", "most_frequent", "constant"],
            ),
            _p("fill_value", None, widget="text", tier="advanced"),
        ],
    ),
    _pre(
        "sklearn.preprocessing.StandardScaler",
        "Standard Scaler",
        [_p("with_mean", True, widget="toggle"), _p("with_std", True, widget="toggle")],
    ),
    _pre(
        "sklearn.preprocessing.MinMaxScaler",
        "MinMax Scaler",
        [_p("feature_range", (0, 1), widget="text", tier="advanced")],
    ),
    _pre(
        "sklearn.preprocessing.OneHotEncoder",
        "One-Hot Encoder",
        [
            _p(
                "handle_unknown",
                "ignore",
                widget="select",
                choices=["error", "ignore", "infrequent_if_exist"],
            ),
            _p("sparse_output", False, widget="toggle", tier="advanced"),
        ],
    ),
    _pre(
        "sklearn.preprocessing.OrdinalEncoder",
        "Ordinal Encoder",
        [
            _p(
                "handle_unknown",
                "use_encoded_value",
                widget="select",
                choices=["error", "use_encoded_value"],
            ),
            _p("unknown_value", -1, widget="int", tier="advanced"),
        ],
    ),
    _pre(
        "sklearn.preprocessing.PolynomialFeatures",
        "Polynomial Features",
        [
            _p("degree", 2, widget="int", min=1, max=5),
            _p("interaction_only", False, widget="toggle", tier="advanced"),
            _p("include_bias", True, widget="toggle", tier="advanced"),
        ],
    ),
    _pre(
        "sklearn.preprocessing.KBinsDiscretizer",
        "KBins Discretizer",
        [
            _p("n_bins", 5, widget="int", min=2, max=100),
            _p(
                "encode",
                "ordinal",
                widget="select",
                choices=["onehot", "onehot-dense", "ordinal"],
            ),
            _p(
                "strategy",
                "quantile",
                widget="select",
                choices=["uniform", "quantile", "kmeans"],
            ),
        ],
    ),
    _pre(
        "sklearn.preprocessing.PowerTransformer",
        "Power Transformer",
        [
            _p("method", "yeo-johnson", widget="select", choices=["yeo-johnson", "box-cox"]),
            _p("standardize", True, widget="toggle", tier="advanced"),
        ],
    ),
    _pre(
        "sklearn.preprocessing.QuantileTransformer",
        "Quantile Transformer",
        [
            _p("n_quantiles", 1000, widget="int", min=10, tier="advanced"),
            _p(
                "output_distribution",
                "uniform",
                widget="select",
                choices=["uniform", "normal"],
            ),
            _p("random_state", None, widget="int", tier="advanced"),
        ],
    ),
    _pre(
        "sklearn.impute.KNNImputer",
        "KNN Imputer",
        [
            _p("n_neighbors", 5, widget="int", min=1),
            _p("weights", "uniform", widget="select", choices=["uniform", "distance"]),
        ],
    ),
    _pre(
        "sklearn.feature_selection.SelectKBest",
        "SelectKBest",
        [
            _p("k", 10, widget="int", min=1),
        ],
    ),
    _pre(
        "sklearn.feature_selection.VarianceThreshold",
        "Variance Threshold",
        [_p("threshold", 0.0, widget="number", min=0.0)],
    ),
]


COMPOSITES: list[ComponentMetadata] = [
    ComponentMetadata(
        qualname="sklearn.pipeline.Pipeline",
        display_name="Pipeline",
        category="composite",
        description="Chain of transformers plus a final estimator.",
        doc_url=f"{_DOC_ROOT}sklearn.pipeline.Pipeline.html",
    ),
    ComponentMetadata(
        qualname="sklearn.compose.ColumnTransformer",
        display_name="Column Transformer",
        category="composite",
        description="Apply different transformer branches to disjoint column groups.",
        doc_url=f"{_DOC_ROOT}sklearn.compose.ColumnTransformer.html",
    ),
    ComponentMetadata(
        qualname="sklearn.pipeline.FeatureUnion",
        display_name="Feature Union",
        category="composite",
        doc_url=f"{_DOC_ROOT}sklearn.pipeline.FeatureUnion.html",
    ),
]


SEARCH: list[ComponentMetadata] = [
    ComponentMetadata(
        qualname="sklearn.model_selection.GridSearchCV",
        display_name="Grid Search CV",
        category="search",
        doc_url=f"{_DOC_ROOT}sklearn.model_selection.GridSearchCV.html",
        params=[
            _p("cv", 5, widget="int", min=2),
            _p("scoring", None, widget="text"),
            _p("n_jobs", None, widget="int", tier="advanced"),
        ],
    ),
    ComponentMetadata(
        qualname="sklearn.model_selection.RandomizedSearchCV",
        display_name="Randomized Search CV",
        category="search",
        doc_url=f"{_DOC_ROOT}sklearn.model_selection.RandomizedSearchCV.html",
        params=[
            _p("cv", 5, widget="int", min=2),
            _p("n_iter", 20, widget="int", min=1),
            _p("scoring", None, widget="text"),
            _p("random_state", None, widget="int", tier="advanced"),
            _p("n_jobs", None, widget="int", tier="advanced"),
        ],
    ),
]

ALL_COMPONENTS: list[ComponentMetadata] = (
    ESTIMATORS + REGRESSORS + TRANSFORMERS + COMPOSITES + SEARCH
)
