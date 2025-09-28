# 定义交易策略函数
from pybroker import ExecContext


def buy_func(ctx: ExecContext) -> None:
    pos = ctx.long_pos()  # 获取当前的长期持有的股票
    # print(pos)
    # print(ctx.date[-1])
    # print(ctx.volume)
    # print(ctx.symbol)
    if pos:  # 如果当前持有股票
        # ctx.sell_shares = pos.shares  # 卖出所有的股票
        # ctx.sell_all_shares() # 卖出全部
        pass
    else:  # 如果当前没有持有股票
        ctx.buy_shares = ctx.calc_target_shares(0.5)  # 买入全部可购买的股票
        # ctx.hold_bars = 120  # 设置持有的交易日为3天
        # ctx.stop_loss_pct = 2  # 百分比止损, 设置止损百分比为2%
        # ctx.stop_profit_pct = 5  # 设置止盈百分比为5%
        ctx.stop_trailing_pct = 1  # 移动止损, 最高市场价格下降N%时触发止损

        # 当触发止损时，希望股票以不低于这个限价的价格卖出
        # 这里设置为当前收盘价减 2，意味着当股票价格下跌到当前收盘价减去 2 的价位时，触发止损并且以不低于这个价格的条件卖出股票
        # 确保在一个相对理想的价格执行止损操作
        # ctx.stop_loss_limit = ctx.close[-1] - 2  # 设置止损价格为当前价格减去100元
