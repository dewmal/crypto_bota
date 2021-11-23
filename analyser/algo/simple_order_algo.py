from analyser.algo.order_algo import OrderAlgo, OrderExecutor


class SimpleOrderAlgo(OrderAlgo):

    def __init__(self, symbol, order_executor: OrderExecutor, number_of_orders=1, options: dict = None):
        super().__init__(symbol, order_executor, number_of_orders, options)

    async def get_buy_point(self, price_list, options):
        return self.identify_buy_point(price_list, options["p_ab"], options["p_bc"])

    async def get_sell_point(self, price_list, options):
        return self.identify_sell_point(price_list, options["p_de"], options["p_ef"])

    def identify_buy_point(self, prices, p_ab, p_bc):
        w_is, w_ie = 0, len(prices) - 1
        c, b, a = w_ie, w_ie, w_ie
        cv = prices[c]
        for i in reversed(range(len(prices))):
            bv = prices[i]
            change = (cv - bv) * 100 / bv
            if p_ab > change > p_bc:
                b = i
                break
        if c > b:
            for i in reversed(range(b)):
                av = prices[i]
                change = (av - bv) * 100 / av
                if change > p_ab:
                    a = i
                    break
        if c > b > a:
            return c, [a, b, c]
        return False, None

    def identify_sell_point(self, prices, p_de, p_ef):
        w_is, w_ie = 0, len(prices) - 1
        f, e, d = w_ie, w_ie, w_ie
        fv = prices[f]
        for i in reversed(range(len(prices))):
            ev = prices[i]
            change = (ev - fv) * 100 / ev
            if p_de > change > p_ef:
                e = i
                break
        if f > e:
            for i in reversed(range(e)):
                dv = prices[i]
                change = (ev - dv) * 100 / ev
                if change > p_de:
                    d = i
                    break
        if f > e > d:
            return f, [d, e, f]
        return False, None
