### 1단계 : Anchorbox의 Pc값과 클래스 확률 곱하기

Anchorbox의 Pc값에는 물체가 있을 확률이 있습니다. 그리고 c1, c2에는 각각의 클래스에 속할 확률이 있습니다.
이 확률을 곱하여 물체가 있을 법한 확률을 의미하는 Objectness와 클래스에 속할 확률 Class confidence 두 가지를 모두 충족시키는 박스만 남도록 합니다.
![image](https://cdn-api.elice.io/api-attachment/attachment/ceb97194b6c74503ac543689df033a2f/image.png)

두 확률을 곱하면 아래와 같이 박스당 2개 (Anchorbox가 두 개이므로)씩 총 8개의 박스 후보가 나옵니다. 각 후보 박스에는 클래스별 Class confidence 값 c1과 c2 정보가 남아있게 됩니다.
![image](https://cdn-api.elice.io/api-attachment/attachment/00d7891f83374e3f974cfb9a4f9b9b44/image.png)

### 2단계 : 확률값 Threshold값 걸고 정렬

문제에서 주어진 대로, Pc와 클래스에 속할 확률과 클래스에 속할 확률의 곱에 Threshold = 0.2를 적용해 0.2 미만인 좌표들은 0을 대입하여 박스를 탈락시킵니다.
![image](https://cdn-api.elice.io/api-attachment/attachment/e6e9cd42894e48f6be086807f2791762/image.png)

***\*탈락 후 모습\****
![image](https://cdn-api.elice.io/api-attachment/attachment/1d50a450f726453682999b590a31a11e/image.png)

이후, 클래스별로 (c1, c2에 대해 각각) 값이 높은 순서대로 정렬합니다. (내림차순 정렬)

***\*클래스 c1의 정렬 후 모습\****
![img](https://cdn-api.elice.io/api-attachment/attachment/da2e22cee3ec48b2aeefa7bafda8460d/image.png)

***\*클래스 c2의 정렬 후 모습\****
![img](https://cdn-api.elice.io/api-attachment/attachment/b284684dacc641ef9a799cc6add16a63/image.png)

### 3단계 : IoU Threshold : 문제 조건에 따라 패스합니다.

### 4단계 : 가장 최고 점수를 가지고 있는 박스만 걸러내기

정렬 후 박스는 다음과 같이 남습니다.
![img](https://cdn-api.elice.io/api-attachment/attachment/77c8c25c30044a50bcfdf4ce9a573c4e/image.png)

클래스별 박스의 번호가 겹치지 않으므로 각각의 박스는 최고로 높은 클래스 점수를 이미 하나씩만 가지고 있게 됩니다. 따라서 정답 박스는 3개입니다.
![img](https://cdn-api.elice.io/api-attachment/attachment/9fa200a986a8470f8805044f154b2629/image.png)