print("Boletim de notas \n")


nome = input("Qual seu nome: ")
curso = input("Qual seu curso: ")
semestre = input("qual seu semestre: ")
disciplina = input("qual disciplina: ")
nota = int(input("qual nota: "))

if nota > 19 and nota < 60: 
    print("recuperação")


elif nota >= 60: 
    print("aprovado!")


else: 
    print("reprovado!")
