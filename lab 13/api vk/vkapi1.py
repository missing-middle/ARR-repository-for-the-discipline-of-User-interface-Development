import vk_api

def predict_user_age(user_id):
    # Авторизация
    vk_session = vk_api.VkApi(token='Ваш токен')
    vk = vk_session.get_api()
    
    # Получаем информацию о друзьях пользователя
    friends = vk.friends.get(user_id=user_id, fields='bdate')
    
    ages = []
    for friend in friends['items']:
        if 'bdate' in friend:
            bdate = friend['bdate'].split('.')
            if len(bdate) == 3:
                age = 2022 - int(bdate[2])
                ages.append(age)
    
    if len(ages) > 0:
        predicted_age = sum(ages) // len(ages)
        return predicted_age
    else:
        return "Недостаточно данных для прогнозирования возраста"

# Пример использования
user_id = '186287124'
predicted_age = predict_user_age(user_id)
print(f"Прогнозируемый возраст пользователя: {predicted_age}")