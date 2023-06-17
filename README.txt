Для запуска требуются:
- Docker (для установки https://www.docker.com/products/docker-desktop/)
- Скачаный проект

Запуск контейнера:

1. Запустить CMD в дириктиве проекта

2. Выполнить команду:

    docker build -t pytest_runner .

    (не забываем про точку в конце команды)

2. Выполнить команду:

     docker run --rm --mount type=bind,src=[директива с докер файлом],target=/test_project/ pytest_runner

         --rm - ключ для автоматического удаления контейнера после выполнения
         --mount - подтягивание тестов из проекта

3. Результаты тестов выводятся в консоль

Если вам необходим вывод не в консоль, а в log файл в Dockerfile измените строку

CMD pytest -s -v

на

CMD pytest -s -v >output.log

далее выполните команду

docker image rm pytest_runner

и повторите действия с шага 2