def ativo(nome_ativo, nome_resp,vulnerabilidade=''):
    if vulnerabilidade:
        print(f"O ativo '{nome_ativo}' possui a vulnerabilidade '{vulnerabilidade}', o nome do responsável por tal ativo é '{nome_resp}'")
    else:
        print(f"O ativo '{nome_ativo}' não possui nenhuma vulnerabilidade cadastrada, o nome do responsável por tal ativo é '{nome_resp}'")

#ativo("Computador", "Lucas", "Roubo")
ativo("Computador", "Lucas")
