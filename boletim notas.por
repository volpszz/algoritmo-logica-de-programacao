programa {
  funcao inicio() {
    
  escreva("boletim notas")
  cadeia nome
  cadeia curso
  cadeia semestre
  cadeia disciplina
  inteiro nota

  escreva("\n Nome do(a) Aluno(a): ")
  leia(nome)

  escreva(" \nQual seu curso?: ")
  leia(curso)

  escreva("\nQual seu semestre?: ")
  leia(semestre)

  escreva("\nQual discplina?: ")
  leia(disciplina)

  escreva("\nQual Nota?: ")
  leia(nota)

  se (nota > 19 e nota < 60){
    escreva("recuperação")
  }

   senao se (nota >= 60){
    escreva("aprovado!")
  }

  senao{
    escreva("reprovado!")
  }

  }
}
