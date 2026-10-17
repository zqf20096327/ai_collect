# Simple Neural Network

Простая реализация полносвязной нейронной сети на Java для образовательных целей, демонстрирующая ключевые концепции глубокого обучения.

## Описание

Этот проект реализует базовую архитектуру нейронной сети с поддержкой:
- Прямого распространения (forward propagation)
- Обратного распространения (backpropagation)
- Обновления весов (weight updates)
- Различных функций активации (sigmoid и производная)
- Классификации на датасетах Iris и Wine

Сеть предназначена для обучения и понимания фундаментальных принципов работы нейронных сетей.

## Возможности

- Создание полносвязной нейронной сети произвольной архитектуры
- Обучение на размеченных данных
- Валидация и оценка качества модели
- Нормализация данных (Feature Scaling)
- Поддержка различных функций активации
- Гибкая конфигурация скорости обучения
- Кэширование выходных значений для оптимизации

## Архитектура

### Основные компоненты

```
Network
├── Layer[]
│   ├── Neuron[]
│   │   ├── weights[]
│   │   ├── delta
│   │   ├── learningRate
│   │   └── activationFunction
│   └── outputCache[]
└── Methods
    ├── train() - обучение
    ├── validate() - валидация
    ├── outputs() - прямое распространение
    └── backPropagate() - обратное распространение
```

### Ключевые классы

| Класс | Описание |
|-------|---------|
| `Network<T>` | Главный класс нейронной сети |
| `Layer` | Слой нейронов |
| `Neuron` | Отдельный нейрон с весами и функцией активации |
| `Activation` | Функции активации (sigmoid и производная) |
| `Normalize` | Нормализация данных методом Feature Scaling |
| `Iris` / `Wine` | Классификаторы для датасетов |

## Быстрый старт

### Требования

- Java 11 или выше
- Maven 3.6+

### Установка

```bash
# Клонировать репозиторий
git clone https://github.com/Lewickiy/simple-neural.git
cd simple-neural

# Собрать проект
mvn clean compile
```

### Использование

#### Пример классификации Iris

```java
Iris iris = new Iris();
Network<String>.Results results = iris.classify();
System.out.println("Точность: " + (results.percentage * 100) + "%");
System.out.println("Правильных: " + results.correct + " из " + results.trials);
```

#### Пример классификации Wine

```java
Wine wine = new Wine();
Network<Integer>.Results results = wine.classify();
System.out.println("Точность: " + (results.percentage * 100) + "%");
```

#### Тестирование на 1000 итераций

```java
int iterations = 1000;
double totalAccuracy = 0.0;

for (int i = 0; i < iterations; i++) {
    Wine wine = new Wine();
    Network<Integer>.Results results = wine.classify();
    totalAccuracy += results.percentage;
}

double averageAccuracy = (totalAccuracy * 100) / iterations;
System.out.println("Средняя точность: " + averageAccuracy + "%");
```

## Структура проекта

```
simple-neural/
├── src/main/java/com/lewickiy/
│   ├── Main.java                          # Главный класс с примерами
│   ├── neuronnetwork/
│   │   ├── Network.java                   # Основной класс сети
│   │   ├── Layer.java                     # Слой нейронов
│   │   └── Neuron.java                    # Отдельный нейрон
│   ├── classification/
│   │   ├── Iris.java                      # Классификатор Iris
│   │   └── Wine.java                      # Классификатор Wine
│   └── util/
│       ├── Activation.java                # Функции активации
│       ├── Normalize.java                 # Нормализация данных
│       ├── MaxDoubleList.java             # Утилиты для работы с массивами
│       ├── Weight.java                    # Работа с весами
│       ├── Counter.java                   # Счетчики слоев и нейронов
│       └── LoadLearnedWeights.java        # Загрузка весов (в разработке)
├── iris                                   # Датасет Iris
├── wine                                   # Датасет Wine
├── pom.xml                                # Конфигурация Maven
└── README.md                              # Этот файл
```

## Конфигурация

### Параметры обучения

Скорость обучения и функции активации можно настраивать при создании слоев:

```java
Layer layer = new Layer(
    previousLayer,           // Предыдущий слой (Optional)
    numNeurons,             // Количество нейронов
    learningRate,           // Скорость обучения (рекомендуется 0.1 - 0.5)
    activationFunction,     // Функция активации
    derivativeActivationFunction  // Производная функции активации
);
```

### Функции активации

```java
// Sigmoid функция активации (используется по умолчанию)
double output = Activation.sigmoid(x);
double derivative = Activation.derivativeSigmoid(x);
```

## Принцип работы

### 1. Прямое распространение (Forward Propagation)

```
Input → Layer1 → Layer2 → ... → Output
```

Каждый нейрон вычисляет:
```
output = activation(weights · inputs + bias)
```

### 2. Обратное распространение (Backpropagation)

Вычисление дельт (ошибок) для каждого слоя:
- Выходной слой: `δ = f'(z) × (ŷ - y)`
- Скрытые слои: `δ = f'(z) × Σ(δ_next × weights_next)`

### 3. Обновление весов

```
w_new = w_old + learning_rate × layer_input × δ
```

## Тестирование

Проект включает JUnit 4 для модульного тестирования:

```bash
# Запустить тесты
mvn test

# Запустить с отчетом по покрытию (JaCoCo)
mvn clean test
```

## Датасеты

### Iris Dataset
- Классы: 3 (setosa, versicolor, virginica)
- Признаки: 4 (длина чашелистика, ширина, длина лепестка, ширина лепестка)
- Выборка: 150 примеров

### Wine Dataset
- Классы: 3 (Wine 1, Wine 2, Wine 3)
- Признаки: 13 (различные химические показатели)
- Выборка: 178 примеров

## Нормализация данных

Для улучшения обучения используется нормализация методом Feature Scaling:

```java
List<double[]> data = loadData();
Normalize.normalizeByFeatureScaling(data);
```

Формула: `x_norm = (x - min) / (max - min)`

## Образовательная ценность

Этот проект демонстрирует:
- Базовую архитектуру нейронной сети
- Реализацию алгоритма обратного распространения ошибки
- Применение функций активации
- Работу с весами и обновлениями
- Процесс обучения и валидации
- Нормализацию входных данных

Идеален для студентов и начинающих, изучающих основы машинного обучения и нейронных сетей.

## В разработке

- Загрузка и сохранение обученных весов
- Поддержка дополнительных функций активации (ReLU, Tanh)
- Визуализация процесса обучения
- Оптимизация производительности
- Параллельные вычисления

## Примечания

### Скорость обучения
- Слишком большая скорость может привести к расходимости
- Слишком маленькая скорость замедляет сходимость
- Рекомендуемый диапазон: 0.1 - 0.5

### Архитектура сети
Для датасета Iris хорошо работает архитектура:
```
Input (4) → Hidden (8) → Hidden (6) → Output (3)
```

Для датасета Wine:
```
Input (13) → Hidden (16) → Hidden (12) → Output (3)
```

## Лицензия

Проект распространяется по лицензии MIT. Подробности см. в файле LICENSE.

## Контакты

Автор: Lewickiy

Если у вас есть вопросы или предложения, откройте Issue или свяжитесь через GitHub.

## Благодарности

Спасибо всем, кто вносит свой вклад в развитие этого образовательного проекта!
