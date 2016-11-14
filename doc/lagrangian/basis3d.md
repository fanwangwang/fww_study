
# 3D case 

| Notation | Meaning |
|:-----|:------|
|$$\tau$$ | a tet |
|$$x_1, x_2, x_3, x_4$$ | the four vertices |
|$$e_{ij} := (x_i, x_j)$$ | the edge |
|$$f_{ijk} := (x_i, x_j, x_k)$$ | the face | 
|$$\lambda_1, \lambda_2, \lambda_3, \lambda_4$$ | The barycenter coordinates|

Let us discuss the $$p$$ order basis.

* basis functions on the four vertices
* basis functions on the six edges
* basis functions on the four faces
* basis functions in the interior of tet

The basis function on $$x_i$$:
$$
\phi_i = \frac{p^{p}}{p!}\Pi_{l=0}^{p-1}
(\lambda_i - \frac{l}{p}), 
$$
where $$i = 1, 2, ,3 ,4$$.

The the basis function on $$e_{ij}$$: 

$$
\phi_{ij, m} = \frac{p^p}{m!(p-m)!}
\Pi_{l_1 = 0}^{m-1}(\lambda_i  - \frac{l_1}{p})
\Pi_{l_2 = 0}^{p-m-1}(\lambda_j - \frac{l_2}{p}),
$$

where $$i \not= j$$

The basis functions on $$f_{ijk}$$:
$$
\phi_{ijk,m,n} = \frac{p^p}{m!n!(p-m-n)!}\Pi_{l_1 = 0}^{m - 1}
(\lambda_i - \frac{l_1}{p}) \Pi_{l_2 = 0}^{n-1}(\lambda_j -
\frac{l_2}{p}) \Pi_{l_3=0}^{p-m-n-1}(\lambda_k - \frac{l_3}{p}).
$$


The basis functions in $$\tau$$:
$$
\begin{aligned}
\phi_{1234, m, n, t} = &\frac{p^p}{m!n!t!(p-m-n-t)!}
\Pi_{l_1 = 0}^{m - 1} (\lambda_1 - \frac{l_1}{p})
\Pi_{l_2 = 0}^{n-1}(\lambda_2 - \frac{l_2}{p})\\
&\Pi_{l_3=0}^{t - 1 }(\lambda_3 - \frac{l_3}{p})
\Pi_{l_4=0}^{k - m - n - t - 1}(\lambda_4 - \frac{l_4}{p}.
\end{aligned}
$$

