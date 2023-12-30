def hitung_rating(rating):
    terendah = min(rating)
    tertinggi = max(rating)
    average = sum(rating) / len(rating)
    return [terendah, tertinggi, average]

input1 = [4.5, 2.0, 1.5, 3.0, 2.5, 4.0, 5.0, 3.5, 2.0, 1.0]
output1 = hitung_rating(input1)
print(output1)

input2 = [5.0, 4.0, 2.5, 5.0, 3.6, 1.1, 3.6, 4.0, 4.2, 1.5]
output2 = hitung_rating(input2)
print(output2)