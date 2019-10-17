
from RL_brain import DeepQNetwork
import time, requests, json
import numpy as np



class Web_env(object):
    def __init__(self, host="http://127.0.0.1:9090"):
        self.host = host
        self.n_actions = 4
        self.n_features = 2


    def reset(self):
        url = self.host + "/game_tools"
        data =  {
            "op" : "reset"

        }

        rsp = requests.post(url, data=data)
        #print(rsp.text)

        rsp = rsp.json()

        return np.array(rsp['now_pos'])

    
    def render(self):

        pass


    def step(self, action):
        url = self.host + "/game_tools"

        dir = ["up", "down", "left", "right"]
        data = {
            "op" : "set_position",
            "dir" : dir[action]
        }

        rsp = requests.post(url, data=data)
        
        rsp = rsp.json()
        #print(rsp['now_pos'], dir[action])
        return np.array(rsp['now_pos']), rsp['reward'], rsp['done']



def run_maze():
    step = 0
    for episode in range(300):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            RL.store_transition(observation, action, reward, observation_)

            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1

    # end of game
    print('game over')
    #env.destroy()


if __name__ == "__main__":
    # maze game
    env = Web_env()
    RL = DeepQNetwork(env.n_actions, env.n_features,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=2000,
                      # output_graph=True
                      )
    while True:
        run_maze()
        time.sleep(1)