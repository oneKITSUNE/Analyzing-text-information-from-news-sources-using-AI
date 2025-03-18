<h1 align="center"> Дипломная работа </h1>
<h3 align="center"> Анализ текстовой информации из новостных источников с помощью нейросетей </h3>

Добро пожаловать в репозиторий моей дипломной работы! Этот проект посвящён анализу текстовой информации из новостных источников с использованием нейронных сетей. В рамках работы я разработала систему, которая позволяет анализировать текстовые файлы формата `.txt` с помощью нейросети **GigaChat**. Взаимодействие с системой осуществляется через **Telegram-бота**.

## Описание проекта
### Цель проекта: 
Создание инструмента для автоматизированного анализа текстовой информации из новостных источников. Нейросеть GigaChat используется для обработки и анализа текстовых данных, что позволяет извлекать основные идеи и тезисы, классифицировать информацию.

### Основные функции:
- Загрузка и обработка текстовых файлов формата `.txt`.
- Анализ текста с использованием нейросети GigaChat.
- Взаимодействие с пользователем через Telegram-бота.
- Возможность перехода на популярные новостные сайты (ТАСС, РИА Новости, Дзен) прямо из бота.

## Описание начала работы с ботом

1. **Установка зависимостей**  
   Перед началом работы убедитесь, что у вас установлены все необходимые зависимости. Для этого выполните команду:
   ```bash
   pip install telebot requests
   ```

2. **Настройка Telegram-бота**  
   - Создайте бота в Telegram с помощью [BotFather](https://core.telegram.org/bots#botfather).
   - Получите токен вашего бота и добавьте его в переменную `API_TOKEN` в файле `main.py`.

3. **Настройка GigaChat**  
   - Получите API-ключ для доступа к GigaChat и добавьте его в переменную `GIGA_CHAT_API_KEY` в файле `main.py`.

## Как найти бота в Telegram?

Чтобы начать работу с ботом, выполните следующие шаги:

1. **Поиск бота в Telegram**:
   - Откройте Telegram и введите имя бота в поисковой строке. Имя бота: `@News_analysis_with_AI_bot`.
   - Нажмите на бота в результатах поиска.

2. **Ссылка на бота**:
   - Вы также можете перейти к боту напрямую, перейдя по ссылке: [Telegram](https://t.me/News_analysis_with_AI_bot).

3. **Запуск бота**:
   - После перехода к боту отправьте команду `/start`, чтобы активировать его.

Теперь вы готовы использовать бота для анализа текстовых файлов!

 ## Инструкция по использованию
1. После запуска бота отправьте команду `/start` в Telegram.
2. Выберите одну из опций: переход на новостные сайты (ТАСС, РИА Новости, Дзен) или загрузку текстового файла для анализа.
3. Если вы выбрали загрузку файла, отправьте боту файл формата `.txt`. Бот обработает его с помощью нейросети GigaChat и вернёт результат анализа.

## Требования к файлам

Для корректной работы бота и анализа текста с помощью нейросети GigaChat, **текстовый файл (.txt) должен быть в кодировке UTF-8**. Это обеспечивает правильное чтение и обработку текста, особенно если он содержит символы кириллицы или другие специальные символы.

### Как проверить и изменить кодировку файла:

   - Откройте файл в текстовом редакторе (например, Notepad++, VS Code или Блокнот).
   - Убедитесь, что кодировка указана как UTF-8. В Notepad++ это можно проверить в меню "Кодировка" → "Преобразовать в UTF-8".
   - Если файл сохранён в другой кодировке (например, ANSI или Windows-1251), преобразуйте его в UTF-8.

### Почему это важно?

Нейросеть GigaChat и бот корректно работают только с текстом в кодировке UTF-8. Использование других кодировок может привести к ошибкам при чтении файла или искажению текста.

## Пример работы бота

1. **Запуск бота**:  
   Пользователь отправляет команду `/start`, и бот предлагает выбрать опцию: переход на новостные сайты или загрузку файла.

2. **Загрузка файла**:  
   Пользователь выбирает опцию "Хотите загрузить файл TXT?" и отправляет файл. Бот анализирует его с помощью GigaChat и возвращает результат.

3. **Переход на новостные сайты**:  
   Пользователь выбирает один из новостных сайтов (ТАСС, РИА Новости, Дзен), и бот предоставляет ссылку для перехода.

## Контакты
Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной:  
Мой **[Telegram](https://t.me/oneKITSUNE)**

Спасибо за внимание! 🚀
