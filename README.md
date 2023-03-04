# Binomial Expansion Desktop App (GUI with PyQt5)

This application uses the unknown-terms library for math operations. You can create terms and view their binomial expansions.

### How to use the binomial expansion program ?
- Installation
You have to install unknown-terms library.
```shell
pip install unknown-terms
```
If you already have the library, you should use the last version
```shell
pip install unknown-terms --upgrade
```

Let's look at the [binomial_expansion.py](https://github.com/lightningcell/binomial-expansion/blob/master/binomial_expansion.py "binomial_expansion.py") :

```python
def binomial_expansion(term1, term2, exponent) -> str:
    """:return (term1 + term2) ^^ exponent"""
```
The parameters term1 and term2 can be; int, float, AlphaTerm or MultipleAlphaTerm. This function returns the exponent(th) power of sum the term1 and term2.

```python
t1 = AlphaTerm()  # x
t2 = AlphaTerm(_alpha="y", _coe=-1)  # -y
t3 = AlphaTerm(-3, "x", 1)  # -3x ^^ 1
t4 = AlphaTerm(10, "z", 2)  # 10z ^^ 2
mt1 = t1 * t2  # -xy
mt2 = t3 * t4  # -30(x^^4)(z^^2)

print(binomial_expansion(t1, t2, 2))
print(binomial_expansion(t3, t4, 3))
print(binomial_expansion(mt1, t3, 4))
print(binomial_expansion(t1, t3, 4))
print(binomial_expansion(mt1, mt2, 5))
```
Let's look at the results:
```powershell
[1] x² - 2xy + y²
[2] - 27x³ + 270x²z² - 900xz⁴ + 1000z⁶
[3] x⁴y⁴ + 12x⁴y³ + 54x⁴y² + 108x⁴y + 81x⁴
[4] +16x⁴
[5] - x⁵y⁵ - 150x⁵y⁴z² - 9000x⁵y³z⁴ - 270000x⁵y²z⁶ - 4050000x⁵yz⁸ - 24300000x⁵z¹⁰
```
That's it ! Using the unknown-terms library in this app, makes it easier to control the flow.

**Term generation with regular expressions will be added to the app later.**

## GUI 
- Installation
You must have downloaded PyQt5 to be able to use this application.

```shell
pip install PyQt5
```

- Run
```shell
>>> cd ../binomial-expansion
>>> python app.py
```

- Term Creator

*You can create AlphaTerm objects in this page.*

<p align='center'><a  href="https://www.linkpicture.com/view.php?img=LPic640366eb7b95b139922122"><img width=400 src="https://www.linkpicture.com/q/app1.png" type="image"></a></p>

*When the regular expression update complete, this part will be enable*
<p align='center'><a href="https://www.linkpicture.com/view.php?img=LPic64036a5dd780b877356016"><img width=400 src="https://www.linkpicture.com/q/app2.png" type="image"></a></p>

- Created Terms

*You can see the terms, that you created in the Term Creator page. After next update, the values will be changeable*
<p align='center'><a href="https://www.linkpicture.com/view.php?img=LPic64036b6de97781183797079"><img width=400 src="https://www.linkpicture.com/q/app3.png" type="image"></a></p>

- Binomial Expansion


<div align="center">
  <video src="https://user-images.githubusercontent.com/117159961/222916568-db70afd6-9dbb-4aab-94c0-5ae7b22b8b47.mp4" width=400/>
<div/>
