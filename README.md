### Hexlet tests and linter status:
[![Actions Status](https://github.com/shtoporrr/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shtoporrr/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/f1cd298c58de5bdf18d3/maintainability)](https://codeclimate.com/github/shtoporrr/python-project-49/maintainability)

Brain Games

Приложение включает 5 игр для развития логического мышления, памяти и аналитических навыков:

1. Четность – проверка на четность числа.
2. Калькулятор – вычисление результата математического выражения.
3. Делитель – нахождение наибольшего общего делителя двух чисел.
4. Прогрессия – определение пропущенного числа в арифметической прогрессии.
5. Простые числа – проверка числа на простоту.

Каждая игра начинает с запроса имени пользователя, затем предлагает ответить на 3 вопроса. При верном ответе игра продолжается, а при неверном – сразу завершается с указанием правильного результата. При прохождении всех раундов игрок побеждает и получает поздравление. Повторить игру можно, запустив её заново или выбрав другую.

Иструкция по установке:

1. Клонирование репозитория:
    git clone https://github.com/shtoporrr/python-project-49.git
    cd python-project-49

2. Установка зависимостей с использованием <a href="https://docs.astral.sh/uv/" target="_blank">uv</a>:
    uv sync

3. Сборка пакета:
    make build

4. Установка пакета:
    uv tool install --force dist/*.whl


Запуск игр:

1. brain-even -- запуск игры Четность
2. brain-calc -- запуск игры Калькулятор
3. brain-gcd -- запуск игры Делитель
4. brain-progression -- запуск игры Прогрессия
5. brain-prime -- запуск игры Простые числа

Правила игр.

1. Четность -- пользователяю необходимо ответить yes или no на вопрос "Данное число является четным". Числа показываются случайным образом. 
2. Калькулятор -- пользователю нужно посчитать случайное выражение и ввести правильный ответ. Выражение соержит умножение, сложение, вычитание двух чисел.
3. Делитель -- пользователю необходимо правильно определить и ввести число, являющиеся общим делителем двух случайных чисел.
4. Прогрессия -- дана случайная арифметическая прогрессия с одним скрытым числом. Пользователю нужно определить это число и дать правильный ответ. Числа в прогрессии, их количество и спрятанное число выбираеться случайным образом.
5. Простые числа -- пользователю нужно определить являеться ли случно показанное число простым и ввести ответ yes или no.

Демо игр показана ниже:

brain-even:

<a href="https://asciinema.org/a/DxKi0BtKDZu24wSacgzL4MWCO" target="_blank"><img src="https://asciinema.org/a/DxKi0BtKDZu24wSacgzL4MWCO.svg" /></a>

brain-calc:

<a href="https://asciinema.org/a/1nXOExxcOQQi09kMPkMwdOwln" target="_blank"><img src="https://asciinema.org/a/1nXOExxcOQQi09kMPkMwdOwln.svg" /></a>

brain-gcd:

<a href="https://asciinema.org/a/TvzTZPqrOl865Lh41Eb4xnfEp" target="_blank"><img src="https://asciinema.org/a/TvzTZPqrOl865Lh41Eb4xnfEp.svg" /></a>

brain-progression:

<a href="https://asciinema.org/a/OfBatVr7DnxWNfYlFH3wJPyZY" target="_blank"><img src="https://asciinema.org/a/OfBatVr7DnxWNfYlFH3wJPyZY.svg" /></a>

brain-prime:

<a href="https://asciinema.org/a/1Gj8kijE6g3iHurjuIMvg4tr2" target="_blank"><img src="https://asciinema.org/a/1Gj8kijE6g3iHurjuIMvg4tr2.svg" /></a>
