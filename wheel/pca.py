class PCA(object):

    def fit(self, X, n_components):
        n_samples, n_features = X.shape

        self.mean_ = np.mean(X, axis=0)
        X -= self.mean_

        # X = U*S*V^T
        # 注意下方S是上方S主对角线上元素
        U, S, V = np.linalg.svd(X, full_matrices=False)

        explained_variance_ = (S ** 2) / (n_samples - 1)
        total_var = explained_variance_.sum()
        explained_variance_ratio_ = explained_variance_ / total_var
        singular_values_ = S.copy()

        components_ = V

        self.n_samples_, self.n_features_ = n_samples, n_features
        self.components_ = components_[:n_components]
        self.n_components_ = n_components
        self.explained_variance_ = explained_variance_[:n_components]
        self.explained_variance_ratio_ = \
            explained_variance_ratio_[:n_components]
        self.singular_values_ = singular_values_[:n_components]

        return U, S, V

    def transform(self, X):
        X -= self.mean_

        print('transform: X.shape is {0} \ncomponents shape is {1}'.format(X.shape, self.components_.shape))
        red_x = np.dot(X, self.components_.T)

        return red_x

    def fit_transform(self, X, n_components):
        U, S, V = self.fit(X, n_components)
        U = U[:, :self.n_components_]
        print('fit_transform U S V shape is {0}, {1}, {2}'.format(U.shape, S.shape, V.shape))

        # red_x = X * V = U*S*V^T  * V = U*S
        red_x = U * S[:n_components]

        return red_x

    def decomposition_cov(self, X, n_components):
        x_mean_ = np.mean(X, axis=0)
        X -= x_mean_

        x_cov = np.cov(X, rowvar=0)

        # 对比array和mat的乘法
        eig_vals, eig_vects = np.linalg.eig(np.mat(x_cov))

        eig_vals_idx = np.argsort(eig_vals)
        eig_vals_idx = eig_vals_idx[:-(n_components + 1):-1]

        self.eig_vals = eig_vals[eig_vals_idx]
        self.eig_vects = eig_vects[:, eig_vals_idx]

        red_x = X * self.eig_vects

        return red_x


