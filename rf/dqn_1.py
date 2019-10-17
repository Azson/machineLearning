import numpy as  np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt


class DeepQNetwork:
    # 上次的内容
    def _build_net(self):

        pass

    # 这次的内容:
    # 初始值
    def __init__(
            self,
            n_actions,
            n_features,
            learning_rate=0.01,
            reward_decay=0.9,
            e_greedy=0.9,
            replace_target_iter=300,
            memory_size=500,
            batch_size=32,
            e_greedy_increment=None,
            output_graph=False,
    ):
        pass

    # 存储记忆
    def store_transition(self, s, a, r, s_):

        pass

    # 选行为
    def choose_action(self, observation):

        pass

    # 学习
    def learn(self):

        pass

    # 看看学习效果 (可选)
    def plot_cost(self):

        pass


if __name__ == "__main__":

    print("Hello!")
    print("World!")
    print("\rssss")
    