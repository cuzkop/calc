# my first python cli tool

## 目的

- 機械学習(勾配降下法)の勉強兼pythonの勉強のアウトプット

### 勾配降下法とは

- 二次関数において底を求める
- ある初期値xと学習率を決める
- そのxから学習率に従ってグラフの底に向かって進む
- 変化量が少なくなった時点で終了
- 計算式は以下

`次のx = 今のx - (学習率　* 現在の傾き)`


## 機能説明

- 関数は`x^2 - 2x + 3`を想定
- 第一引数に現在の現在のx、第二引数に学習率を渡す
- 傾きが1.0001になるまでループを回す。
- 傾きの経過とループの合計回数を出力
- 使用例は以下

`python calc.py 5 0.1`

## Purpose

- output of studyng mchine learning and python

### description

- f(x) = x^2 - 2x + 3
- first args = current x
- second args = learning rate
- print Inclination history and loop count


