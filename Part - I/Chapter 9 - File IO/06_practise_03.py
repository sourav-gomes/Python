for i in range(2, 21):
    with open(f"/home/joseph/Downloads/python/Chapter 9 - File IO/tables/Multiplication_table_for_{i}.txt", 'w') as f:
        for j in range(1, 13):
            f.write(f"{i}x{j}={i*j}")
            if j != 12:
                f.write('\n')
    