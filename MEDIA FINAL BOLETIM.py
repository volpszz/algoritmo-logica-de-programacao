print("boletim notas")

nome = input("\n Nome do(a) Aluno(a): ")
curso = input(" \nQual seu curso?: ")
semestre = input("\nQual seu semestre?: ")
disciplina = input("\nQual discplina?: ")
nota = float(input("\nQual Nota 1 bi: "))
nota2 = float(input("\nQual Nota 2 bi: "))

media_final = (nota + nota2) / 2.0

if media_final == 67.0:
    print(f"\n | nome:  {nome}\n | curso:  {curso}\n | semestre:  {semestre}\n | discplina:  {disciplina}\n | media final:  {media_final}\n | Resultado:  FARMOU AURA! 6767!!!")
elif media_final >= 6.0 and media_final <= 100.0:
    print(f"\n | nome:  {nome}\n | curso:  {curso}\n | semestre:  {semestre}\n | discplina:  {disciplina}\n | media final:  {media_final}\n | Resultado:  APROVADO!")
elif media_final < 6.0 and media_final > 19.0:
    print(f"\n | nome:  {nome}\n | curso:  {curso}\n | semestre:  {semestre}\n | discplina:  {disciplina}\n | media final:  {media_final}\n | Resultado:  RECUPERAÇÃO!")
elif media_final > 100.0:
    print("VALOR INVALIDO!")
else:
    print(f"\n | nome:  {nome}\n | curso:  {curso}\n | semestre:  {semestre}\n | discplina:  {disciplina}\n | media final:  {media_final}\n | Resultado:  REPROVADO!")
