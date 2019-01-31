def average_grade(roster):
    sum=0
    n=0
    for each in roster:
        sum += each.get_grade()
        n += 1
    return float(sum)/float(n)
