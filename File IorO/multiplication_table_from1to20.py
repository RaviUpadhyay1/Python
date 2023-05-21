for i in range(1,21):
    #     with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
    with open("tables/Multiplication_table_of_"+str(i)+".txt", 'w') as f:
        for j in range(1,11):
            f.write(str(i)+"x"+str(j)+"="+str(i*j))
            #f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write("\n")