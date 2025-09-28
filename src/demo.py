import pybroker
from pybroker.ext.data import AKShare
from pybroker import ExecContext, StrategyConfig, Strategy
from pybroker.ext.data import AKShare
import matplotlib.pyplot as plt
from strategy.base_strategy import buy_func

#  启用数据源:akshare 并开启缓存
akshare = AKShare()
pybroker.enable_data_source_cache('akshare')

start_date = '20250115'  # 或者: 8/15/2025
end_date = '20250930'
symbol1 = '000001.SZ'  # 平安银行  或者 000001.SZ
symbol2 = '600000.SH'  # 浦发银行  或者 600000.SH

# 获取股票数据
# 你可以用000001替换000001.SZ，程序仍然可以正常运行！
# 并且你可以将起始日期设置为“20210301”这种格式。
# 你还可以将“adjust”设置为“qfq”（前复权）或“hfq”（后复权）来调整数据，
# 并将“timeframe”设置为“1d”（日数据）、“1w”（周数据）以获取每日、每周的数据。
df = akshare.query(
    symbols=[symbol1, symbol2],
    start_date=start_date,
    end_date=end_date,
    adjust="hfq",
    timeframe="1d",
)
print(df)

df = akshare.query(symbols=symbol1, start_date=start_date, end_date=end_date, adjust='')
print(df)

# 创建策略配置对象，设置初始现金为 500,000 元
my_config = StrategyConfig(initial_cash=500000)

# 创建策略对象，设置数据源为 AKShare，开始日期为 '20230801'，结束日期为 '20230830'，策略配置为 my_config
strategy = Strategy(data_source=AKShare(), start_date=start_date, end_date=end_date, config=my_config)

# 将定义的交易策略函数添加到策略对象中，应用于股票 '000001'
strategy.add_execution(fn=buy_func, symbols=[symbol1])

# 执行回测
result = strategy.backtest(warmup=3)

result.portfolio.equity.plot()

# print(result.orders)
print(result.metrics_df)

# 查看买卖交易操作记录
print(f'result.orders:\n{result.orders}')

# 查看收益
# print(f'result.portfolio:\n{result.portfolio}')

result.portfolio.equity.plot()  # 查看资金的变化情况
plt.show()  # 启动 matplotlib 的事件循环，使图形窗口保持显示
