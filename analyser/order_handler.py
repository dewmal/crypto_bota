class OrderHandler:

    def __init__(self):
        pass

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
