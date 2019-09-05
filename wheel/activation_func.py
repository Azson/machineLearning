
#pca study https://github.com/scikit-learn/scikit-learn/blob/1495f6924/sklearn/decomposition/pca.py#L104


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def step_fuc(x):
    return 1 if x > 0 else 0 if x == 0 else -1