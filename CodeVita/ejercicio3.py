def maximize_gems(n, dishes):
    ratings = [0]

    for dish in dishes:
        id, rating = map(int, dish.split(':'))
        
        ratings.append(max(ratings[-1] + rating, rating))

    return max(ratings)

n = int(input())
dishes = input().split()

result = maximize_gems(n, dishes)
print(result)
