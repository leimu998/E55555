def cal_precision_recall(truel_label, pre_label):
    precision = defaultdict(int)  # 查准
    recall = defaultdict(int)  # 查全
    total = defaultdict(int)  # 总数
    for t, p in zip(truel_label, pre_label):
        total[t] += 1
        recall[p] += 1
        if t == p:  # 全
            precision[t] += 1  # 准

    # for label in precision.keys():
    for label in range(1, max(y_true) + 1):
        rec = precision[label] / total[label]
        pre = precision[label] / recall[label] if label in recall else 0
        F1 = (2 * pre * rec) / (pre + rec) if pre + rec else 0
        print(f"{str(label)}  precision: {str(pre)}  recall: {str(rec)}  F1: {str(F1)}")

    pre = rec = toa = 0
    # 计算去全部的
    for label in range(1, max(y_true) + 1):
        pre += precision[label]
        toa += total[label]
        rec += recall[label]

    pres = pre / rec
    recs = pre / toa
    F1 = (2 * pres * recs) / (pres + recs) if pres + recs else 0
    print(f"All:  precision: {str(pres)}  recall: {str(recs)}  F1: {str(F1)}")


y_true = [1, 2, 3]
y_pred = [1, 1, 3]
cal_precision_recall(y_true, y_pred)
