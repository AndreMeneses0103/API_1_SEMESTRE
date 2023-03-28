# Integrante para integrante
# Sprint 4

muito_ruim = 0
ruim = 0
regular = 0
bom = 0
muito_bom = 0

nota = int(input("\nComo você avalia a comunicação do(a) X com o grupo durante o desenvolvimento do projeto?\n"))
nota = int(input("\nComo você avalia o trabalho em equipe do(a) X durante o desenvolvimento do projeto?\n"))
nota = int(input("\nComo você avalia a proatividade do(a) X durante o desenvolvimento do projeto?\n"))
nota = int(input("\nComo você avalia a produtividade do(a) X durante o desenvolvimento do projeto?\n"))
nota = int(input("\nComo você avalia a entrega do(a) X com relação ao prazo no desenvolvimento do projeto?\n"))

if (nota == 1):
    muito_ruim = muito_ruim + 1
if (nota == 2):
    ruim = ruim + 1
if (nota == 3):
    regular = regular + 1
if (nota == 4):
    bom = bom + 1
if (nota == 1):
    muito_bom = muito_bom + 1            


