# [level 0] rny_string - 181863 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181863) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 11월 16일 14:41:01

### 문제 설명

<p>'m'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다. 문자열 <code>rny_string</code>이 주어질 때, <code>rny_string</code>의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>rny_string</code>의 길이 ≤ 100</li>
<li><code>rny_string</code>은 영소문자로만 이루어져 있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>rny_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"masterpiece"</td>
<td>"rnasterpiece"</td>
</tr>
<tr>
<td>"programmers"</td>
<td>"prograrnrners"</td>
</tr>
<tr>
<td>"jerry"</td>
<td>"jerry"</td>
</tr>
<tr>
<td>"burn"</td>
<td>"burn"</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>rny_string</code>의 'm'을 "rn"으로 바꾸는 과정을 표로 나타내면 다음과 같습니다.</li>
</ul>

<p>|rny_string|m|a|s|t|e|r|p|i|e|c|e|</p>

<p>|---------|-|-|-|-|-|-|-|-|-|-|-|</p>

<p>|result|rn|a|s|t|e|r|p|i|e|c|e|</p>
<div class="highlight"><pre class="codehilite"><code>따라서 "rnasterpiece"를 return 합니다.
</code></pre></div>
<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>rny_string</code>의 'm'을 "rn"으로 바꾸는 과정을 표로 나타내면 다음과 같습니다.</li>
</ul>

<p>|rny_string|p|r|o|g|r|a|m|m|e|r|s|</p>

<p>|---------|-|-|-|-|-|-|-|-|-|-|-|</p>

<p>|result|p|r|o|g|r|a|rn|rn|e|r|s|</p>
<div class="highlight"><pre class="codehilite"><code>따라서 "prograrnrners"를 return 합니다.
</code></pre></div>
<p>입출력 예 #3</p>

<ul>
<li>예제 3번의 <code>rny_string</code>에는 'm'이 없습니다. 따라서 <code>rny_string</code> 그대로인 "jerry"를 return 합니다.</li>
</ul>

<p>입출력 예 #4</p>

<ul>
<li>예제 4번의 <code>rny_string</code>에는 'm'이 없습니다. 따라서 <code>rny_string</code> 그대로인 "burn"를 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges