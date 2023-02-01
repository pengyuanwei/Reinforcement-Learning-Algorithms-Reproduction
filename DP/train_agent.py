from cliff_walking_env import CliffWalkingEnv
from policy_iteration import PolicyIteration
from value_iteration import ValueIteration


def print_agent(agent, action_meaning, disaster=[], end=[]):
    print("状态价值：")
    for i in range(agent.env.nrow-1, -1, -1):
        for j in range(agent.env.ncol):
            # 为了输出美观,保持输出6个字符
            print('%6.6s' % ('%.3f' % agent.v[i * agent.env.ncol + j]), end=' ')
        print()

    print("策略：")
    for i in range(agent.env.nrow-1, -1, -1):
        for j in range(agent.env.ncol):
            # 一些特殊的状态,例如悬崖漫步中的悬崖
            if (i * agent.env.ncol + j) in disaster:
                print('****', end=' ')
            elif (i * agent.env.ncol + j) in end:  # 目标状态
                print('EEEE', end=' ')
            else:
                a = agent.pi[i * agent.env.ncol + j]
                pi_str = ''
                for k in range(len(action_meaning)):
                    pi_str += action_meaning[k] if a[k] > 0 else 'o'
                print(pi_str, end=' ')
        print()


env = CliffWalkingEnv()
action_meaning = ['v', '^', '<', '>']
theta = 0.001
gamma = 0.9

# agent = PolicyIteration(env, theta, gamma)
# agent.policy_iteration()

agent = ValueIteration(env, theta, gamma)
agent.value_iteration()

print_agent(agent, action_meaning, list(range(37, 47)), [47])   # 此时打印的是最优价值函数，它是基于最优策略的。最优策略不会移动至悬崖，因此价值函数不会受到掉入悬崖奖励-100的影响。
