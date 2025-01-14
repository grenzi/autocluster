class Constants(object):
    default_general_metafeatures = [
        "numberOfInstances",
        "logNumberOfInstances",
        "numberOfFeatures",
        "logNumberOfFeatures",
        "isMissingValues",
        "numberOfMissingValues",
        "missingValuesRatio",
        "sparsity",
        "datasetRatio",
        "logDatasetRatio"
    ]
    default_numeric_metafeatures = [
        "sparsityOnNumericColumns",
        "minSkewness",
        "maxSkewness",
        "medianSkewness",
        "meanSkewness",
        "firstQuartileSkewness",
        "thirdQuartileSkewness",
        "minKurtosis",
        "maxKurtosis",
        "medianKurtosis",
        "meanKurtosis",
        "firstQuartileKurtosis",
        "thirdQuartileKurtosis",
        "minCorrelation",
        "maxCorrelation",
        "medianCorrelation",
        "meanCorrelation",
        "firstQuartileCorrelation",
        "thirdQuartileCorrelation",
        "minCovariance",
        "maxCovariance",
        "medianCovariance",
        "meanCovariance",
        "firstQuartileCovariance",
        "thirdQuartileCovariance",
        "PCAFractionOfComponentsFor95PercentVariance",
        "PCAKurtosisFirstPC",
        "PCASkewnessFirstPC",
    ]