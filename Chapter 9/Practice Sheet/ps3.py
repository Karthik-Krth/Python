def gen_mul_tab(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n*i} \n"
    with open(f"tables/table{n}.txt","w") as f :
        f.write(table)



for n in range(2,31):
    gen_mul_tab(n)