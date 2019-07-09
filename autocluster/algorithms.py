from sklearn import cluster 
from smac.configspace import ConfigurationSpace
from ConfigSpace.hyperparameters import CategoricalHyperparameter, \
UniformFloatHyperparameter, UniformIntegerHyperparameter

class algorithms(object):
    # this class is just to create an extra layer of namespace
    
    class Metaclass(type):
        # metaclass to ensure that static variables in the classes below are read-only
        @property
        def name(cls):
            return cls._name

        @property
        def model(cls):
            return cls._model

        @property
        def params(cls):
            return cls._params

        @property
        def params_names(cls):
            return cls._params_names

    class DBSCAN(object, metaclass=Metaclass):
        # static variables
        _name = "DBSCAN"
        _model = cluster.DBSCAN
        _params = [
            UniformFloatHyperparameter("eps", 0.01, 10, default_value=2.0),
            UniformIntegerHyperparameter("min_samples", 5, 1000, default_value=100)
        ]
        _params_names = set([p.name for p in _params])

    class KMeans(object, metaclass=Metaclass):
        # static variables
        _name = "KMeans"
        _model = cluster.KMeans
        _params = [
            UniformIntegerHyperparameter("n_clusters", 1, 20, default_value=10)
        ]
        _params_names = set([p.name for p in _params]) 
        
    class MiniBatchKMeans(object, metaclass=Metaclass):
        # static variables
        _name = "MiniBatchKMeans"
        _model = cluster.MiniBatchKMeans
        _params = [
            UniformIntegerHyperparameter("n_clusters", 1, 20, default_value=10),
            UniformIntegerHyperparameter("batch_size", 10, 1000, default_value=100)
        ]
        _params_names = set([p.name for p in _params]) 
    
    class AffinityPropagation(object, metaclass=Metaclass):
        # static variables
        _name = "AffinityPropagation"
        _model = cluster.AffinityPropagation
        _params = [
            UniformFloatHyperparameter("damping", 0.5, 1, default_value=0.5)
        ]
        _params_names = set([p.name for p in _params]) 
        
    class MeanShift(object, metaclass=Metaclass):
        # static variables
        _name = "MeanShift"
        _model = cluster.MeanShift
        _params = [
            CategoricalHyperparameter("bin_seeding", [True, False], default_value=False)
        ]
        _params_names = set([p.name for p in _params]) 
        
    class SpectralClustering(object, metaclass=Metaclass):
        # static variables
        _name = "SpectralClustering"
        _model = cluster.SpectralClustering
        _params = [
            UniformIntegerHyperparameter("n_clusters", 1, 20, default_value=10),
            CategoricalHyperparameter("eigen_solver", [None,'arpack','lobpcg',\
                                                       'amg'], default_value=None),
            CategoricalHyperparameter("affinity", ['nearest_neighbors', 'precomputed',\
                                                   'rbf'], default_value='rbf')
        ]
        _params_names = set([p.name for p in _params])
        
    class AgglomerativeClustering(object, metaclass=Metaclass):
        # static variables
        _name = "AgglomerativeClustering"
        _model = cluster.AgglomerativeClustering
        _params = [
            UniformIntegerHyperparameter("n_clusters", 1, 20, default_value=10),
            CategoricalHyperparameter("affinity", ['euclidean', 'l1', 'l2', 'manhattan',\
                                                   'cosine', 'precomputed', 'cityblock'],\
                                      default_value='euclidean'),
            CategoricalHyperparameter("linkage", ['complete', 'average', 'single'],\
                                      default_value='complete')
            #'ward' is not added yet.
        ]
        _params_names = set([p.name for p in _params]) 
        
    class OPTICS(object, metaclass=Metaclass):
        # static variables
        _name = "OPTICS"
        _model = cluster.OPTICS
        _params = [
            UniformIntegerHyperparameter("min_samples", 5, 1000, default_value=100),
            UniformFloatHyperparameter("max_eps", 0.01, 10, default_value=2.0),
            CategoricalHyperparameter("metric", ['euclidean', 'l1', 'l2', 'manhattan',\
                                                   'cosine', 'cityblock', 'braycurtis',\
                                                 'canberra', 'chebyshev', 'correlation',\
                                                 'dice', 'hamming', 'jaccard', 'kulsinski',\
                                                 'mahalanobis', 'minkowski', 'rogerstanimoto',\
                                                 'russellrao', 'seuclidean', 'sokalmichener', \
                                                 'sokalsneath', 'sqeuclidean', 'yule'],\
                                      default_value='minkowski'),
            CategoricalHyperparameter("cluster_method", ['xi', 'dbscan'], default_value='xi')
        ]
        _params_names = set([p.name for p in _params])
        
    class Birch(object, metaclass=Metaclass):
        # static variables
        _name = "Birch"
        _model = cluster.Birch
        _params = [
            UniformIntegerHyperparameter("n_clusters", 1, 20, default_value=10)
        ]
        _params_names = set([p.name for p in _params]) 
