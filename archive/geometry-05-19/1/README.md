# Теорема косинусов. Вид треугольника (остроугольный, тупоугольный). Теорема синусов.
## Теорема косинусов
![Доказательство т. кос.](cos.jpg)
## Теорема синусов
![Доказательство т. син.](sin.jpg)

<h4 id="header_6">Случай треугольника: доказательство</h4>
    <p>Приведём здесь элементарное доказательство, не использующее теорию интегралов. </p>
    <p>Первым подобное, чисто геометрическое, доказательство привёл Архимед, но оно было весьма сложным, с большим
        числом геометрических построений. Приведённое здесь доказательство взято из статьи Apostol, Mnatsakanian
        "Finding Centroids the Easy Way".</p>
    <p>Доказательство сводится к тому, чтобы показать, что центр масс треугольника лежит на одной из медиан; повторяя
        этот процесс ещё дважды, мы тем самым покажем, что центр масс лежит в точке пересечения медиан, которая и есть
        центроид.</p>
    <p>Разобьём данный треугольник <img class="tex" src="../tex2png/cache/0e738dc1c640233f2c460e261c522f78.png" alt="T">
        на четыре, соединив середины сторон, как показано на рисунке:</p>
    <p><img src="/algo/centroids_1.jpg"></p>
    <p>Четыре получившихся треугольника подобны треугольнику <img class="tex"
            src="../tex2png/cache/0e738dc1c640233f2c460e261c522f78.png" alt="T"> с коэффициентом <img class="tex"
            src="../tex2png/cache/e8c10a24565fd4a9da8e3ea9e464fec9.png" alt="1/2">.</p>
    <p>Треугольники №1 и №2 вместе образуют параллелограмм, центр масс которого <img class="tex"
            src="../tex2png/cache/58390d91c72a3448176ac07726eb622b.png" alt="c_{12}"> лежит в точке пересечения его
        диагоналей (поскольку это фигура, симметричная относительно обеих диагоналей, а, значит, её центр масс обязан
        лежать на каждой из двух диагоналей). Точка <img class="tex"
            src="../tex2png/cache/58390d91c72a3448176ac07726eb622b.png" alt="c_{12}"> находится посередине общей стороны
        треугольников №1 и №2, а также лежит на медиане треугольника <img class="tex"
            src="../tex2png/cache/0e738dc1c640233f2c460e261c522f78.png" alt="T">:</p>
    <p><img src="/algo/centroids_2.jpg"></p>
    <p>Пусть теперь вектор <img class="tex" src="../tex2png/cache/e77f13f6d02eabc9ec2e5ced8ce6cd22.png" alt="\vec{r}"> —
        вектор, проведённый из вершины <img class="tex" src="../tex2png/cache/b5f17df636a8bd667d2f5c3404ed82e7.png"
            alt="A"> к центру масс <img class="tex" src="../tex2png/cache/b06d49dbb8e3290786f17ec1eb3a24d7.png"
            alt="c_1"> треугольника №1, и пусть вектор <img class="tex"
            src="../tex2png/cache/c7813586615133f30dc6bea31d47d020.png" alt="\vec{m}"> — вектор, проведённый из <img
            class="tex" src="../tex2png/cache/b5f17df636a8bd667d2f5c3404ed82e7.png" alt="A"> к точке <img class="tex"
            src="../tex2png/cache/58390d91c72a3448176ac07726eb622b.png" alt="c_{12}"> (которая, напомним, является
        серединой стороны, на которой она лежит):</p>
    <p><img src="/algo/centroids_3.jpg"></p>
    <p>Наша цель — показать, что вектора <img class="tex" src="../tex2png/cache/e77f13f6d02eabc9ec2e5ced8ce6cd22.png"
            alt="\vec{r}"> и <img class="tex" src="../tex2png/cache/c7813586615133f30dc6bea31d47d020.png" alt="\vec{m}">
        коллинеарны.</p>
    <p>Обозначим через <img class="tex" src="../tex2png/cache/b6cdefa6632857f6103c69e89d63959b.png" alt="c_3"> и <img
            class="tex" src="../tex2png/cache/fa7e7d621fc814616d39ab07ab2122b0.png" alt="c_4"> точки, являющиеся
        центрами масс треугольников №3 и №4. Тогда, очевидно, центром масс совокупности этих двух треугольников будет
        точка <img class="tex" src="../tex2png/cache/23a227f74feb4eedcf0c70ea6ab2a5a2.png" alt="c_{34}">, являющаяся
        серединой отрезка <img class="tex" src="../tex2png/cache/9b19f5c25331fe6a005fb01006ba1aab.png" alt="c_3 c_4">.
        Более того, вектор от точки <img class="tex" src="../tex2png/cache/58390d91c72a3448176ac07726eb622b.png"
            alt="c_{12}"> к точке <img class="tex" src="../tex2png/cache/23a227f74feb4eedcf0c70ea6ab2a5a2.png"
            alt="c_{34}"> совпадает с вектором <img class="tex"
            src="../tex2png/cache/e77f13f6d02eabc9ec2e5ced8ce6cd22.png" alt="\vec{r}">.</p>
    <p>Искомый центр масс <img class="tex" src="../tex2png/cache/fdabaa70e1c423d289836bd4624e9e4e.png" alt="c">
        треугольника <img class="tex" src="../tex2png/cache/0e738dc1c640233f2c460e261c522f78.png" alt="T"> лежит
        посередине отрезка, соединяющего точки <img class="tex"
            src="../tex2png/cache/58390d91c72a3448176ac07726eb622b.png" alt="c_{12}"> и <img class="tex"
            src="../tex2png/cache/23a227f74feb4eedcf0c70ea6ab2a5a2.png" alt="c_{34}"> (поскольку мы разбили треугольник
        <img class="tex" src="../tex2png/cache/0e738dc1c640233f2c460e261c522f78.png" alt="T"> на две части равных
        площадей: №1-№2 и №3-№4):</p>
    <p><img src="/algo/centroids_4.jpg"></p>
    <p>Таким образом, вектор от вершины <img class="tex" src="../tex2png/cache/b5f17df636a8bd667d2f5c3404ed82e7.png"
            alt="A"> к центроиду <img class="tex" src="../tex2png/cache/fdabaa70e1c423d289836bd4624e9e4e.png" alt="c">
        равен <img class="tex" src="../tex2png/cache/897bfceedc0f2bdf16c23b7a2b6a0912.png" alt="\vec{m} + \vec{r}/2">. С
        другой стороны, т.к. треугольник №1 подобен треугольнику <img class="tex"
            src="../tex2png/cache/0e738dc1c640233f2c460e261c522f78.png" alt="T"> с коэффициентом <img class="tex"
            src="../tex2png/cache/e8c10a24565fd4a9da8e3ea9e464fec9.png" alt="1/2">, то этот же вектор равен <img
            class="tex" src="../tex2png/cache/90433486bbbfd8a677d534cddcb371e5.png" alt="2 \vec{r}">. Отсюда получаем
        уравнение:</p>
    <p></p>
    <p class="formula"><img class="tex" src="../tex2png/cache/0a64e37d9a9f82228c533a4c73e7b658.png"
            alt=" \vec{m} + \vec{r}/2 = 2 \vec{r}, "></p>
    <p>откуда находим:</p>
    <p></p>
    <p class="formula"><img class="tex" src="../tex2png/cache/b94ea7dec62339a6463f3cf5462b8ea5.png"
            alt=" \vec{r} = \frac{2}{3} \vec{m}. "></p>
    <p>Таким образом, мы доказали, что вектора <img class="tex"
            src="../tex2png/cache/e77f13f6d02eabc9ec2e5ced8ce6cd22.png" alt="\vec{r}"> и <img class="tex"
            src="../tex2png/cache/c7813586615133f30dc6bea31d47d020.png" alt="\vec{m}"> коллинеарны, что и означает, что
        искомый центроид <img class="tex" src="../tex2png/cache/fdabaa70e1c423d289836bd4624e9e4e.png" alt="c"> лежит на
        медиане, исходящей из вершины <img class="tex" src="../tex2png/cache/b5f17df636a8bd667d2f5c3404ed82e7.png"
            alt="A">.</p>
    <p>Более того, попутно мы доказали, что центроид делит каждую медиану в отношении <img class="tex"
            src="../tex2png/cache/0b6584d85913c7cc17f605523732ffc7.png" alt="2:1">, считая от вершины.</p>
    <p></p>
    <p></p>
    <p></p><a name="7"></a>

{% include lib/mathjax.html %}
