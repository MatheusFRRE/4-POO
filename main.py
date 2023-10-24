from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from cursos import Curso

def main():
    pessoaFisica1 = PessoaFisica("Eduardo", "51999999999", "Rua X", "1999", "12345678")
    pessoaJuridica1 = PessoaJuridica("Empresa X", "51888888888", "Rua Y", "1234567/0001")
    cursos1 = Curso("Curso de Python", 120)
    print(pessoaFisica1)
    print(pessoaJuridica1)
    print(cursos1)

if __name__ == "__main__":
    main()