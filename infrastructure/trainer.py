import pandas as pd
import numpy as np


def collaborative_filtering(users_data, prompts_data, n_recommendations=10):
    """
    协同过滤算法，基于用户行为数据推荐可用的prompt
    :param users_data: DataFrame, 包含用户的性别和年龄信息
    :param prompts_data: DataFrame, 包含prompt的记录和相关信息
    :param n_recommendations: int, 需要推荐的prompt数量
    :return: DataFrame, 推荐的prompt列表
    """
    # 对于每个用户，计算平均年龄、性别，并创建空的prompt记录列表
    user_info = users_data.groupby('user_id').agg({'age': np.mean, 'gender': np.mean})
    user_info['prompts'] = [list() for i in range(len(user_info))]

    # 对于每个prompt记录，将其与相应用户的记录列表进行比较，如果用户记录中有相同的prompt，则将该记录的得分增加1
    for index, prompt in prompts_data.iterrows():
        user_id = prompt['user_id']
        if user_id in user_info.index:
            if prompt['prompt'] in user_info.loc[user_id, 'prompts']:
                user_info.loc[user_id, 'prompts'][prompt['prompt']] += 1
            else:
                user_info.loc[user_id, 'prompts'][prompt['prompt']] = 1

    # 对于每个用户，将其记录列表按得分从高到低排序，并选择前N个得分最高的记录作为推荐的prompt列表
    recommended_prompts = []
    for user_id, user_data in user_info.iterrows():
        user_prompts = user_data['prompts']
        sorted_prompts = sorted(user_prompts.items(), key=lambda x: x[1], reverse=True)
        recommended_prompts.extend(sorted_prompts[:n_recommendations])

    # 返回推荐的prompt列表
    return pd.DataFrame(recommended_prompts, columns=['prompt', 'score'])
