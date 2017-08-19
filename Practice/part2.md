<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
# markdown 练习
1.对样本向量进行归一化处理后, 计算三个属性(字段2 字段3 字段5)的相关性, 归一化处理的公式为
$$\vec x_{norm}=\frac{\vec x-\overline{x}}{\left \Vert \vec x-\overline{x} \right \Vert_2}$$
通过点积(或者协方差矩阵)计算相关性即可，归一化后的协方差矩阵为
$$\left[ \begin{matrix} 1&0.9994&-0.5791 \\\ 0.9994&1&-0.5495 \\\ -0.5791&-0.5495&1 \end{matrix} \right]$$
可以发现字段2, 字段3之间有强相关, 而和字段5基本不相关


