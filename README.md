## Little Lemon API

### API Эндпоинты
- `GET /api/menu/` - получить список блюд
- `POST /api/menu/` - добавить блюдо (нужен токен)
- `GET /api/bookings/` - получить список бронирований (нужен токен)
- `POST /api/bookings/` - забронировать столик (нужен токен)

### Тестирование API
1. Войти в систему (Insomnia, Postman) с учетными данными суперпользователя
2. Тестировать эндпоинты с токеном авторизации
