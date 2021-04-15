# Implementation of evidence theory (D-S theory)

Evidence theory is an effective tool to make decision from ambiguity, which has been widely used in target recognition, decision making, optimization problem. Compared with ANN, combination result can be achieved without training process. Traditionally, weight of each evidence should be computed before obtaining a reasonable combination result [https://www.onacademic.com/detail/journal_1000040883012810_0724.html](https://www.onacademic.com/detail/journal_1000040883012810_0724.html), [https://www.onacademic.com/detail/journal_1000040419277410_af84.html](https://www.onacademic.com/detail/journal_1000040419277410_af84.html), [ A new conflict management method in Dempster–Shafer theory ](https://www.onacademic.com/detail/journal_1000039865751710_f512.html).

This project is the primary version of evidence combination where evidence weight processing is omitted. And the calculation of evidence weight will be emitted in the next version.

## Getting Started

### Installing

installation via pip is our recommendation:

```
pip install evi
```

## Combine evidences

Evidence should be created before combination:

```python
e1 = Evi(focal_elements=['a', 'b', ['a', 'c'], ], bpas=[0.2, 0.3, 0.5])
```

the code above stands for:
$$
p(a)=0.2\\
p(b)=0.3\\
p(a \space or \space c)=0.5
$$


and we can get the combination result via the following code:

```python
    e1 = Evi(focal_elements=['a', 'b', ['a', 'c'], ], bpas=[0.2, 0.3, 0.5])
    e2 = Evi(focal_elements=['a', 'b', ['a', 'c'], ['b', 'c']], bpas=[0.4, 0.3, 0.1, .2])
    combination_result = e1.combine(e2)
    print(combination_result)
```



additionally, the combination of evidence set is:

```python
    e1 = Evi(focal_elements=['a', 'b', ['a', 'c'], ], bpas=[0.2, 0.3, 0.5])
    e2 = Evi(focal_elements=['a', 'b', ['a', 'c'], ['b', 'c']], bpas=[0.4, 0.3, 0.1, .2])

    es = [e1, e2]
    print(Evi.combine_list(e1, e2, ))
```





## License

This project is licensed under the MIT License

## Acknowledgments

if you wanna to cite this project, the following code may be in your consideration：

```
@misc{TP-toolbox-web,

   author = {qiaokuoyuan},

   title = {evi},

   howpublished = {\url{https://github.com/qiaokuoyuan/evi}}

}
```

