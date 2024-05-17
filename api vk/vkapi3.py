import vk_api
import networkx as nx
import matplotlib.pyplot as plt

# Авторизация в API ВКонтакте
vk_session = vk_api.VkApi(token='Ваш токен')
vk = vk_session.get_api()

def get_friends_ids(user_id):
    friends = vk.friends.get(user_id=user_id)
    return friends['items']

def build_graph(user_ids):
    G = nx.Graph()
    
    for user_id in user_ids:
        friends_ids = get_friends_ids(user_id)
        for friend_id in friends_ids:
            G.add_edge(user_id, friend_id)
    
    return G

user_ids = [186287124, 163713623, 340120551]  # Пример списка айди пользователей

# Создание графа с друзьями пользователей
G = build_graph(user_ids)

# Визуализация графа
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_size=10, font_color='black')
plt.title("Граф друзей в ВКонтакте")
plt.show()