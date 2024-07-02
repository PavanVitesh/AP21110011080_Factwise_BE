# Pavan Vitesh Kuncham - AP21110011080 - Q.No - 7
# cardPoints is a integer list and k is int value
def calculate_sum(cardPoints, k):
    n = len(cardPoints)
    new_lst = cardPoints[n-k:n] + cardPoints[:k]
    m = 0
    for i in range(k):
        m = max(m,sum(new_lst[i:i+k]))
    print(m)