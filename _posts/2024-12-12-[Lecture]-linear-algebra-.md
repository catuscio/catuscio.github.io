---
categories:
- Studies
- Mathematics
date: '2024-12-12'
tags:
- Lecture
- Math
title: '[Lecture] Linear Algebra; 선형대수학'
toc: true
---


### 📐행렬 Tex문법

```latex
\begin{bmatrix}
n & n \\
n & n
\end{bmatrix}
```


# Matrix; 행렬

- 행(Row): 가로 / 열(Column) 세로
- 정방행렬(Square Matrix): 같은 수의 행과 열을 가진 행렬
    - $$\begin{bmatrix} a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{bmatrix}$$.
    - $$a_{11}, a_{22} \cdots, a_{nn}$$을 주 대각선(main diagonal)이라고 한다.



### 🍊예제1

![](/assets/images/lecture-linear_algebra_/image_20241212_044146_a666faef59d042a390be0ebb6b04a2c2.png)

**Sol**

계수행렬(Coefficient matrix): $$\begin{bmatrix}
4 &6&9\\
6&0&-2\\
5&-8&1
\end{bmatrix}$$$$\begin{bmatrix}
x_1\\
x_2\\
x_3 \end{bmatrix}$$=$$\begin{bmatrix}
6\\
20\\
10 \end{bmatrix}$$

첨가행렬(Augmented matrix): $$\begin{bmatrix} 4&6&9& \vert 6\\ 6&0&-2& \vert 20\\5&-8&1& \vert 10 \end{bmatrix}$$

---

## Vector; 벡터

단 하나의 행 or 열 만으로 이루어진 행렬

- 행벡터(Row vector)
    - $$a=\begin{bmatrix} a_1, a_2, \cdots, a_n\end{bmatrix}$$.
- 열벡터(Column vector)
    - $$b=\begin{bmatrix}b_1\\b_2\\ \vdots\\b_m\end{bmatrix}$$.


---

## Matrix Caculation; 행렬연산

- **행렬의 상동**: 두 행렬의 크기가 같고 대응 성분이 같으면 상동

- **행렬의 합**: 크기가 같은 두 행렬 $$A$$와 $$B$$의 합(sum)은 대응 성분끼리 더하고 $$A+B$$로 쓴다.


---
### **행렬의 곱**

$$m \times n$$ 행렬 $$A=[a_{jk}]$$와 $$r\times p$$ 행렬 $$B=[b_{jk}]$$의 곱 $$C=AB$$가 정의될 때, 필요충분조건은 $$r=n$$이며, 이 결과는

$$c_{jk}=\sum_{;=1}^n a_{jl}b_{lk} = a_{j1}b_{1k} + a_{j2}b_{2k}+\cdots+a_{jn}b_{nk}$$

를 성분으로 하는 $$m \times p$$ 행렬 $$C=[c_{jk}]$$로 정한다.

**즉, 앞 행렬의 행에 뒷 행렬의 열을 곱하는 것.**

![](/assets/images/lecture-linear_algebra_/image_20241212_044148_ffacddd23a7b45c8ab4375ebf0ba39f0.png)

>*$$A$$는 $$5\times 3$$ / $$B$$는 $$3 \times 4$$ 이므로 $$C$$는 $$5 \times 4$$ 행렬이다.*

**행렬의 곱은 비가환적(not commutative)이다; **

$$AB \neq BA$$


### 🍊예제

$$A = \begin{bmatrix} 1&2&3\\4&5&6\end{bmatrix} \cdot B=\begin{bmatrix}1&2\\3&4\\5&6\end{bmatrix} = ?$$

**Sol**

$$2 \times 3$$ 행렬과 $$3 \times 2$$ 행렬이므로 결과는 $$2 \times 2$$ 행렬이어야 한다.

$$\begin{bmatrix} 1*1+2*3+3*5 & 1*2+2*4+3*6\\ 4*1+5*3+6*5 & 4*2+5*4+6*6 \end{bmatrix}=\begin{bmatrix}22&28\\49&64\end{bmatrix}$$

---

### 행렬의 전치(Transpose)

$$m \times n$$ 행렬 $$A$$의 전치행렬 $$A^T$$는 $$A$$를 대각선으로 뒤집은 거다.

$$A=[a_{jk}]$$ , $$A^T=[a_{kj}]$$

- **대칭행렬(Symmetric matrix)**
    - $A^T = A$
    - 즉 대칭행렬이려면 정방행렬이어야 한다
- **반대칭행렬(Skew-symmetric matrix)**
    - $A^T=-A$
    - 정방행렬이어야 하고 대각원소는 0이어야 한
- **삼각행렬(Triangular matrix)**
    - 주대각 기준 위 or 아래 원소가 모두 0인 행렬
    - 위삼각행렬(Upper triangular matrix)
    - 아래삼각행렬(lower triangular matrix)
- **대각행렬(Diagonal matrix)**
    - 대각원소 제외 모두 0인 행렬
- **스칼라 행렬(Scalar matrix)**
- **단위행렬(Identity matrix)**
    - $AI = IA = A$


---
## 벡터의 1차 독립과 종속


### 1차 결합(Linear Combination)

같은 수의 성분을 가진 $$m$$개의 벡터 $$a$$에 대하여 이들 벡터의 **1차 결합**이란 스칼라 $$c_1, \cdots, c_m$$에 대하여 다음과 같다.

$$c_1a_{(1)}+c_2a_{(2)}+ \cdots + c_ma_{(m)}$$

**즉, 결합이란 벡터에 스칼라들이 결합되어 있는 것.**


### 1차 독립(Linearly independent)

방정식 $$c_1a_{(1)}+c_2a_{(2)}+ \cdots + c_ma_{(m)} = 0$$에 대하여 $$m$$개의 스칼라 $$c_j$$가 **모두 0인 것이 유일한 해일 때,** 벡터 $$a_{(1)}, \cdots, a_{(m)}$$를 **1차 독립**이라고 한다. 

**즉, 독립이란 벡터와 스칼라들이 서로 독립되어 있는 것.**


### 1차 독립(Linearly dependent)

방정식 $$c_1a_{(1)}+c_2a_{(2)}+ \cdots + c_ma_{(m)} = 0$$에 대하여 $$m$$개의 스칼라 $$c_j$$ 중 **0이 아닌 스칼라가 적어도 하나 존재하면, **벡터 $$a_{(1)}, \cdots, a_{(m)}$$를 **1차 종속**이라고 한다.

**즉, 종속이란 벡터와 스칼라가 서로에 의존하는, 종속되어 있는 것.**

1차 종속인 벡터 집합에서 다른 벡터들의 1차 결합으로 표현되는 벡터들을 소거함으로써, 1차 독립인 벡터들의 집합을 얻을 수 있다.


### 🍊예제

![](/assets/images/lecture-linear_algebra_/image_20241212_044152_6b137065944f4a7d8f0da1ae330d6e13.png)

**Sol**

$$c_1a_1+ c_2a_2 + c_3a_3 = 0$$이어야 하므로 연립방정식을 풀면 $$c_1=c_2=c_3=0$$으로 **독립**이다.

---
### 행렬의 계수(Rank)

행렬에서 1차 독립인 행벡터의 최대 수를 rank라고 하고, rank (행렬)로 표기한다.


### 🍊예제

![](/assets/images/lecture-linear_algebra_/image_20241212_044153_992df82acffb4644adbd284808f313af.png)

**Sol**

<u>간단하게, 가우스 소거법(Gaussian elimination)을 적용하고 영벡터가 아닌 벡터들의 개수를 구하자.</u>

$$A=\begin{bmatrix}3&0&2&2\\0&42&28&58\\0&0&0&0\end{bmatrix}$$ 이므로, **rank 2**이다.

---
## Vector Space; 벡터공간 $$V$$

- **기저(Basis):** $$V$$에 속한 일차독립인 벡터들의 최대 집합을 기저(basis)라고 한다.
- **차원(Dimension):** $$\dim V$$
    - 벡터공간 $$V$$에 속한 일차독립인 벡터들의 최대 수(기저를 구성하는 원소의 개수)
- **생성공간(Span)**
    - 벡터들 $$a_{(1)}, \cdots, a_{(p)}$$이 주어졌을 때, 이들의 일차결합으로 표현되는 모든 벡터들의 집합.
    - $\mathrm{span} \lbrace a_{(1)}, \cdots, a_{(p)} \rbrace = \lbrace c_1a_{(1)} + c_2a_{(2)} + \cdots + c_pa_{(p)} \lVert c_i \in \mathbb{R} \rbrace$
- **행공간(Row space)**: 행렬의 행벡터들의 생성공간을 행공간이라고 한다.
- **열공간(Column space)**: 행렬의 열벡터들의 생성공간을 열공간이라고 한다.
행렬의 행공간과 열공간은 차원이 같고, 이는 행렬의 계수(rank)와 동일하다.

- **영공간(Null space)**: 행렬 $$A$$에 대하여, $$Ax=0$$의 해를 모두 모은 $$x$$의 집합을 $$A$$의 영공간이라고 하며, 이는 벡터 공간이다.

### 🍊예제

![](/assets/images/lecture-linear_algebra_/image_20241212_044154_376939d390bd40ba962e00f4defcab22.png)

**Sol**

- 행렬의 계수: rank 1
- 행공간의 기저: $$\begin{bmatrix} -2&4&-6\end{bmatrix}$$
- 열공간의 기저: $$\begin{bmatrix}-2\\1\end{bmatrix}$$

---
### 선형연립방정식 $$Ax = b$$

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1\\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2\\ \cdots\\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$가 있을 때,


- **존재성(Exixtense)**: $$n$$개의 미지수 $$x_1, \cdots, x_n$$에 관한 $$m$$개의 선형연립방정식이 모순이 없기 위한(consistent), 즉 해를 갖기 위한 필요충분조건은 그 계수행렬 $$A$$와 첨가행렬 $$\tilde A$$이 같은 계수(rank)를 갖는 것이다.
- **유일성(Uniqueness)**: 선형연립방정식이 유일한 해를 갖기 위한 필요충분조건은 $$A$$와 $$\tilde A$$가 같은 계수 $$r=n$$을 갖는 것이다.

---
### Determinant; 행렬식 ($$\det$$)

$$n \times n$$ 정방행렬 $$A=[a_{jk}]$$에 관한 스칼라 값

- $$n=1$$이면 $$D=a_{11}$$으로 정의된다.
- $$n ≥ 2$$이면
    - $$D = a_{j1}c_{j1} + a_{j2}c_{j2}+\cdots+a_{jn}c_{jn}$$ 또는 
$$D=a_{1k}c_{1k}+a_{2k}+c_{2k}+\cdots+a_{nk}c_{nk}$$ ($$j$$는 $$1, 2, \cdots, n$$ 중 하나)
    - $$C_{jk} = (-1)^{j+k}M_{jk}$$ , $$M_{jk}$$는 $$a_{jk}$$를 포함하는 행과
열을 소거하여 얻은 부분행렬의 $$n-1$$차 행렬식
- $$M_{jk}$$를 소행렬식(minor)이라고 부르고 $$C_{jk}$$를 $$a_{jk}$$의 여인수(cofactor)라고 부른다.
- 전개하려고 택하는 열이나 행에 관계없이 행렬식 $$D$$의 값은 같다.

### 🍊예제

![](/assets/images/lecture-linear_algebra_/image_20241212_044155_ecb57dac2ec941e0b36e6cd037664dce.png)

**Sol**

1) 행렬식을 계산할 행을 고른다. $$\begin{bmatrix}1&3&0\end{bmatrix}$$이라 하자.

2) $$\det A = 1 \cdot \begin{bmatrix} 6 & 4 \\ 0 & 2 \end{bmatrix} + (-3) \begin{bmatrix} 2 & 4 \\ -1 & 2 \end{bmatrix} + 0 \cdot \begin{bmatrix} 2 & 6 \\ -1 & 0 \end{bmatrix}$$ 이므로

$$12 + (-3)(8) = -12$$ 이다.


---
### 기본 행연산(elementary row operation) 수행 시 $$n$$차 행렬식의 변화

- 두 행을 바꾸면 행렬식의 값에 $$(-1)$$이 곱해진다.
- 한 행의 상수배를 다른 행에 더하는 것은 행렬식의 값에 변화를 주지 않는다.
- 한 행에 0이 아닌 $$c$$를 곱하면 행렬식의 값이 $$c$$배가 된다.

### $$n$$차 행렬식의 추가적인 성질

- 한 열에 0이 아닌 $$c$$를 곱하면 행렬식의 값이 $$c$$배가 된다.
- 전치(transposition)을 취하여도 행렬식의 값에 변화를 주지 않는다.
- 0행 또는 0열이 있으면 행렬식의 값은 0이다.
- 두 행이나 두 열이 비례관계가 있으면 행렬의 값은 0이다.
- 같은 두 행이나 두 열을 가진 행렬식의 값은 0이다.

---
## 역행렬(Inverse Matrix)

$$n \times n$$행렬 = $$[a_{jk}]$$의 역행렬은 $$A^{-1}$$로 표기하고

- 만약 $$A$$가 역행렬을 가지면, $$A$$**는 정칙행렬(nonsigular matrix)**라고 한다.
    - $$A$$가 역행렬을 가지면 그 역행렬은 유일하다.
    - $$AB = I$$ , $$CA = I$$이면
        - $B=IB=(CA)B=C(AB)=CI=C$
- $$A$$가 역행렬을 갖지 않으면 $$A$$**를 특이행렬(singular matrix)**라고 한다.
