order_status = input("Введите статус заказа: pending, processing, shipped, delivered, cancelled ")

match order_status:
    case "pending":
        status = "В ожидании "
        description = "Ваш заказ принят и ожидает подтверждения"
        emoji= "⏳"
        delivery_time = "2-5минут"
        recommendation = "Дождитесь подтверждения заказа"
    case "processing":
        status = "В обработке "
        description = "Ваш заказ собирается "
        emoji = "🖥"
        delivery_time = "1-3 дня"
        recommendation = "Ждите пока обработается заказ"
    case "shipped":
        status = "Отправлено "
        description = "Ваш заказ  в пути "
        emoji = "🛫"
        delivery_time = "3-7 дней"
        recommendation = "Следите за уведомлениями о доставке"
    case "delivered":
        status = "Доставлено"
        description = "Ваш заказ доставлен"
        emoji= "✔"
        delivery_time = "доставка завершена"
        recommendation = "Проверьте товар и оставьте отзыв"
    case "cancelled":
        status = "Отменено "
        description = "Ваш заказ был отменён"
        emoji= "❌"
        delivery_time = "не требуется"
        recommendation = "Оформите новый заказ "
    case _:
        status = " Ошибка "
        description = "Статус  неизвестно"
        emoji= "❌"
        delivery_time = "неизвестно"
        recommendation = "Доступные статусы: pending, processing, shipped, delivered, cancelled"


print("📦 СТАТУС ВАШЕГО ЗАКАЗА 📦")
print(f"Статус: {status} {emoji}")
print(f"Описание: {description}")
print(f"Примерное время: {delivery_time}")
print(f"Рекомендация: {recommendation}")
