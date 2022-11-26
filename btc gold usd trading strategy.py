def strategy(today_bitcoin_price, tmr_bitcoin_price,
             today_gold_price,tmr_gold_price,
             gold_number,bitcoin_number,dollar_num):
    t=(bitcoin_number * today_bitcoin_price) / (1 + a_bitcoin)
    t+=(gold_number * today_gold_price)/(1 + a_gold)
    dollar_prof = t-(bitcoin_number * today_bitcoin_price + gold_number * today_gold_price)
    if gold_number!=0:
        gold_prof=(gold_number * today_gold_price) * (tmr_gold_price - today_gold_price)/today_gold_price
        bitcoin_prof=(((gold_number * today_gold_price)/(1+a_gold))/(1+a_bitcoin))*(tmr_bitcoin_price - today_bitcoin_price)/today_bitcoin_price
        flag=1
    elif bitcoin_number!=0:
        bitcoin_prof=(bitcoin_number * today_bitcoin_price) * (tmr_bitcoin_price - today_bitcoin_price)/today_bitcoin_price
        gold_prof=(((bitcoin_number * today_bitcoin_price) / (1+a_bitcoin))/(1+a_gold))*((tmr_gold_price - today_gold_price)/today_gold_price)
        flag=2

    else:
        gold_prof = (dollar_num / (1 + a_gold)) *((tmr_gold_price - today_gold_price) / today_gold_price)
        bitcoin_prof = (dollar_num / (1 + a_bitcoin)) *(tmr_bitcoin_price - today_bitcoin_price) / today_bitcoin_price
        flag = 3
    max_prof = max(max(gold_prof, bitcoin_prof), dollar_prof)
    if max_prof < 190:
        return gold_number, bitcoin_number, dollar_num
    if max_prof== gold_prof:
        if flag == 1:
            return gold_number, bitcoin_number, dollar_num
        if flag == 2:
            gold_number += (((bitcoin_number * today_bitcoin_price) / (1 + a_bitcoin)) / (1 + a_gold)) / today_gold_price
            bitcoin_number = 0
            return gold__number, bitcoin_number, dollar_num
        if flag == 3:
                gold_number += (dollar_num / (1+a_gold)) / today_gold_price
                dollar_num = 0
                return gold_number, bitcoin_number, dollar_num
        if max_prof == bitcoin_prof:
            if flag == 1:
                bitcoin_number+=((gold_number * today_gold_price)/(1+a_gold))/(1+a_bitcoin)/today_bitcoin_price
                gold_number=o
                return gold_number,bitcoin_number,dollar_num
            if flag == 2:
                return gold_number,bitcoin_number,dollar_num
            if flag == 3:
                bitcoin_number +=(dollar_num/(1+a_bitcoin))/ today_bitcoin_price
                dollar_num=0
                return gold_number, bitcoin_number, dollar_num
        if max_prof == dollar_prof:
            if flag == 1:
                dollar_num += ((gold_number * today_gold_price)/(1+a_gold))
                gold_number = 0
                return gold_number,bitcoin_number,dollar_num
            if flag == 2:
                dollar_num += ((bitcoin_number * today_bitcoin_price) / (1 + a_bitcoin))
                bitcoin_number = 0
                return gold_number,bitcoin_number,dollar_num
            if flag == 3:
                return gold_number,bitcoin_number, dollar_num