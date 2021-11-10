![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
![Size](https://img.shields.io/github/repo-size/Iamtripathisatyam/100_Days_Code_Challenge?color=red&label=Repo%20Size%20)
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![](https://img.shields.io/tokei/lines/github/Iamtripathisatayam/100_Days_Code_Challenge?color=red&label=Lines%20of%20Code)
![License](https://img.shields.io/badge/License-MIT-red.svg)</br>
![](https://profile-counter.glitch.me/{100_Days_Code_Challenge}/count.svg)

<p align="center">
<img align="center" src="https://github.com/Iamtripathisatyam/iamtripathisatyam/blob/master/Content/manufacturetocat.png" width="300"/>
</p>

<p align="center">
    <img src="https://readme-jokes.vercel.app/api"/>
</p>

_______________________________


### <h1 align="center"><img src="https://img.shields.io/badge/DAY-1-9cf.svg?label=DAY&style=for-the-badge&logo=Python&logoColor=yellow"></h1>
### <ol>Problem 1: <a href="https://github.com/Iamtripathisatyam/100_Days_Code_Challenge/blob/main/DAYS/Day1/Display_Fibonacci_Series.py">**Program to display Fibonacci Series.**</a></ol>
```python
    Input: How Many Terms do you want to Display: 10
    Output: 0 1 1 2 3 5 8 13 21 34
```
### <ol>Problem 2: <a href="https://github.com/Iamtripathisatyam/100_Days_Code_Challenge/blob/main/DAYS/Day1/Factorial_Of_Number.py">**Program to find Factorial of number.**</a></ol>
```python
    Input: Enter a Number: 5
    Output: 5! = 120
```

### <ol>Problem 3: <a href="https://github.com/Iamtripathisatyam/100_Days_Code_Challenge/blob/main/DAYS/Day1/HCF_Of_Number.py">**Program to find HCF of numbers.**</a></ol>
```python
    Input: Enter 1st Number: 5
            Enter 2nd Number: 12
    Output: HCF: 1
```
### <ol>Problem 4: <a href="https://github.com/Iamtripathisatyam/100_Days_Code_Challenge/blob/main/DAYS/Day1/LCM_Of_Number.py">**Program to find LCM of numbers.**</a></ol>
```python
    Input: Enter 1st Number: 5
            Enter 2nd Number: 12
    Output: LCM: 1
```
### <ol>Problem 5: <a href="https://github.com/Iamtripathisatyam/100_Days_Code_Challenge/blob/main/DAYS/Day1/Number_is_Fibonacci_or_not.py">**Program to check whether given number is Fibonacci or not.**</a></ol>
```python
    Input: Enter a Number: 78
    Output: It's not an Fibonacci Number
    
    Input: Enter a Number: 55
    Output: Yup! It's a Fibinacci Number
```

_______________________________

### <h1 align="center"><img src="https://img.shields.io/badge/DAY-59-9cf.svg?label=DAY&style=for-the-badge&logo=Python&logoColor=yellow"></h1>
### <ol>Problem: <a href="https://github.com/Iamtripathisatyam/100_Days_Code_Challenge/blob/main/DAYS/Day59/Arithmetic_Progression_or_not.py">**Program to check a sequence of numbers is an Arithmetic Progression or not.**</a></ol>
```
   ->] Arithmetic Progression or arithmetic sequence is a sequence of numbers such that the difference 
       between the consecutive terms is constant.
```

```python    
    Input: [5, 7, 9, 11]
    Output: True
   
    Input: [5, 8, 9, 11]
    Output: False
    Explanation: The sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression
                 with common difference of 2.
```   
## <h2>**Some Conversions:** </h2>

## <h3 align="center">`Hexadecimal` ---> `Decimal`</h3>
### <ol align="center">3B<sub>16</sub> = 3×16<sup>1</sup> + 11×16<sup>0</sup> = 48 + 11  = 5`<sub>10</sub> , here **B = 11**</ol>

### <ol align="center">E7A9<sub>16</sub> = 14×16<sup>3</sup> + 7×16<sup>2</sup> + 10×16<sup>1</sup> + 9×16<sup>0</sup> = 57344 + 1792 + 160 + 9 = 59305<sub>10</sub> , here **E = 14** & **A = 10**</ol>

### <ol align="center">0.8<sub>16</sub> = 0×16<sup>0</sup> + 8×16<sup>-1</sup> = 0 + 0.5  = 0.5<sub>10</sub></ol>

### <ol align="center">1F.01B<sub>16</sub> = 1×16<sup>1</sup> + 15×16<sup>0</sup> + 0×16<sup>-1</sup> + 1×16<sup>-2</sup> + 11×16<sup>-3</sup> = 31.0065918<sub>10</sub></ol>

## <h3 align="center">`Decimal` ---> `Hexadecimal`</h3>
## <ol>Conversion Steps: </ol>
   - Divide the number by 16.
   - Get the integer quotient for the next iteration.
   - Get the remainder for the hex digit.
   - Repeat the steps until the quotient is equal to 0.
	
## <ol>Example #1: </ol>
### <ol>7562<sub>10</sub><ol/>
	
<img align="right" src="https://github.com/Iamtripathisatyam/iamtripathisatyam/blob/master/Content/rock.gif" width="200"/>	
	
| Division by 16 | Quotient | Remainder | Hex |
| --------------  | ------------- | ------------- | --- |
| 7562 / 16 | 472 | 10 | A |
| 472 / 16  | 29  | 8  | 8 |
| 29 / 16   | 1   | 13 | D |
| 1 / 16    | 0   | 1  | 1 |

### <ol>So, 7562<sub>10</sub> = 1D8A<sub>16</sub><ol/>

## <ol>Example #2: </ol>
### <ol>35631<sub>10</sub><ol/>
	
| Division by 16 | Quotient | Remainder | Hex |
| --------------  | ------------- | ------------- | --- |
| 35631 / 16 | 2226 | 15 | F |
| 2226 / 16  | 139  | 2  | 2 |
| 139 / 16   | 8   | 11 | B |
| 8 / 16    | 0   | 8  | 8 |

### <ol>So, 35631<sub>10</sub> =  8B2F<sub>16</sub><ol/>
	
_______________________________


### <h1 align="center"><img src="https://img.shields.io/badge/DAY-60-9cf.svg?label=DAY&style=for-the-badge&logo=Python&logoColor=yellow"></h1>
### <ol>Problem: <a href="https://github.com/Iamtripathisatyam/100_Days_Code_Challenge/blob/main/DAYS/Day60/Geometric_Progression.py">**Program to check a sequence of numbers is a Geometric Progression or not.**</a></ol>
```
   ->] Geometric Progression or geometric sequence is a sequence of numbers where each term after the first is found by 
       multiplying the previous one by a fixed, non-zero number called the common ratio.
```

```python    
    Input: [2, 6, 18, 54]
    Output: True
   
    Input: [10, 5, 2.5, 1.25]
    Output: False
    
    Input: [5, 8, 9, 11]
    Output: False
    Explanation: The sequence 2, 6, 18, 54, ... is a geometric progression with common ratio 3.
                 Similarly, 10, 5, 2.5, 1.25, ... is a geometric sequence with common ratio 1/2.
```   

_______________________________
	
<p> &copy; 2021 Shahzaib Fardeen </p>
